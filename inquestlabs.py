#!/usr/bin/env python

"""
InQuest Labs Command Line Driver

Usage:
    inquestlabs [options] dfi list
    inquestlabs [options] dfi details <sha256> [--attributes]
    inquestlabs [options] dfi download <sha256> <path> [--encrypt]
    inquestlabs [options] dfi attributes <sha256> [--filter=<filter>]
    inquestlabs [options] dfi search (code|context|metadata|ocr) <keyword>
    inquestlabs [options] dfi search (md5|sha1|sha256|sha512) <hash>
    inquestlabs [options] dfi search (domain|email|filename|filepath|ip|registry|url|xmpid) <ioc>
    inquestlabs [options] dfi sources
    inquestlabs [options] dfi upload <path>
    inquestlabs [options] iocdb list
    inquestlabs [options] iocdb search <keyword>
    inquestlabs [options] iocdb sources
    inquestlabs [options] repdb list
    inquestlabs [options] repdb search <keyword>
    inquestlabs [options] repdb sources
    inquestlabs [options] yara (b64re|base64re) <regex> [(--big-endian|--little-endian)]
    inquestlabs [options] yara hexcase <instring>
    inquestlabs [options] yara uint <instring> [--offset=<offset>] [--hex]
    inquestlabs [options] yara widere <regex> [(--big-endian|--little-endian)]
    inquestlabs [options] lookup ip <ioc>
    inquestlabs [options] lookup domain <ioc>
    inquestlabs [options] report <ioc>
    inquestlabs [options] stats
    inquestlabs [options] setup <apikey>
    inquestlabs [options] trystero list-days
    inquestlabs [options] trystero list-samples <yyyy-mm-dd>

Options:
    --attributes        Include attributes with DFI record.
    --api=<apikey>      Specify an API key.
    --big-endian        Toggle big endian.
    --config=<config>   Configuration file with API key [default: ~/.iqlabskey].
    --debug             Docopt debugging.
    --encrypt           Zip sample with password 'infected' before downloading.
    --filter=<filter>   Filter by attributes type (domain, email, filename, filepath, ip, registry, url, xmpid)
    -h --help           Show this screen.
    --hex               Treat <instring> as hex bytes.
    -l --limits         Show remaining API credits and limit reset window.
    --little-endian     Toggle little endian.
    --offset=<offset>   Specify an offset other than 0 for the trigger.
    --proxy=<proxy>     Intermediate proxy
    --timeout=<timeout> Maximum amount of time to wait for IOC report.
    --verbose=<level>   Verbosity level, outputs to stderr [default: 0].
    --version           Show version.
"""

# python 2/3 compatability.
from __future__ import print_function

try:
    import configparser
except:
    import ConfigParser as configparser

# batteries not included.
import docopt
import requests

# disable ssl warnings from requests.
try:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except:
    pass

# standard libraries.
import multiprocessing
import ipaddress
import hashlib
import random
import time
import json
import sys
import os
import re
# from importlib.metadata import version

# extract version from installed package metadata
__application_name__ = "inquestlabs"
__version__ = "1.2.2"
# __version__ = version(__application_name__)
__full_version__ = f"{__application_name__} {__version__}"

VALID_CAT    = ["ext", "hash", "ioc"]
VALID_EXT    = ["code", "context", "metadata", "ocr"]
VALID_HASH   = ["md5", "sha1", "sha256", "sha512"]
VALID_IOC    = ["domain", "email", "filename", "filepath", "ip", "registry", "url", "xmpid"]
VALID_DOMAIN = re.compile("[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+")

# verbosity levels.
INFO  = 1
DEBUG = 2

########################################################################################################################
def worker_proxy (labs, endpoint, arguments, response):
    """
    proxy function for multiprocessing wrapper used by inquestlabs_api.report()
    """

    response[endpoint] = getattr(labs, endpoint)(*arguments)


########################################################################################################################
class inquestlabs_exception(Exception):
    pass

########################################################################################################################
class inquestlabs_api:
    """
    InQuest Labs API Wrapper
    https://labs.inquest.net
    """

    ####################################################################################################################
    def __init__ (self, api_key=None, config=None, proxies=None, base_url=None, retries=3, verify_ssl=True, verbose=0):
        """
        Instantiate an interface to InQuest Labs. API key is optional but sourced from (in order): argument, environment
        variable, or configuration file. Proxy dictionary is a raw pass thru to python-requests, valid keys are 'http'
        and 'https'.

        :type  api_key:    str
        :param api_key:    API key, optional, can also be supplied via environment variable 'IQLABS_APIKEY'.
        :type  config:     str
        :param config:     Path to configuration file containing API key, default is '~/.iqlabskey'.
        :type  proxies:    dict
        :param proxies:    Optional proxy dictionary to pass down to underlying python-requests library.
        :type  base_url:   str
        :param base_url:   API endpoint.
        :type  retries:    int
        :param retries:    Number of times to attempt API request before giving up.
        :type  verify_ssl: bool
        :param verify_ssl: Toggles SSL certificate verification when communicating with the API.
        :type  verbose:    int
        :param verbose:    Values greater than zero provide increased verbosity.
        """

        # internalize supplied parameters.
        self.api_key     = api_key
        self.base_url    = base_url
        self.config_file = config
        self.retries = retries
        self.proxies     = proxies
        self.verify_ssl  = verify_ssl
        self.verbosity   = verbose

        # internal rate limit tracking.
        self.rlimit_requests_remaining = None   # requests remaining in this rate limit window.
        self.rlimit_reset_epoch_time   = None   # time, in seconds from epoch, that rate limit window resets.
        self.rlimit_reset_epoch_ctime  = None   # same as above, but in ctime human readable format.
        self.rlimit_seconds_to_reset   = None   # seconds to reset time.
        self.api_requests_made         = 0      # keep track of how many API requests we've made.

        # if no base URL was specified, use the default.
        if self.base_url is None:
            self.base_url = "https://labs.inquest.net/api"
            self.__VERBOSE("base_url=%s" % self.base_url, DEBUG)

        # if no config file was supplied, use a default path of ~/.iqlabskey.
        if self.config_file is None:
            self.config_file = os.path.join(os.path.expanduser("~"), ".iqlabskey")

        elif "~" in self.config_file:
            self.config_file = os.path.expanduser(self.config_file)

        self.__VERBOSE("config_file=%s" % self.config_file, DEBUG)

        # if an API key was specified, note the source.
        if self.api_key:
            self.api_key_source = "supplied"

        # otherwise, we don't have an API source yet, we'll check the environment and config files though.

        else:
            self.api_key_source = "N/A"

            # check the environment for one
            self.api_key = os.environ.get("IQLABS_APIKEY")

            if self.api_key:
                self.api_key_source = "environment"

            # if we still don't have an API key, try loading one from the config file.
            else:

                # config file format:
                #   $ cat .iqlabskey
                #   [inquestlabs]
                #   apikey: deadbeefdeadbeefdeadbeefdeadbeefdeadbeef
                if os.path.exists(self.config_file) and os.path.isfile(self.config_file):

                    config = configparser.ConfigParser()

                    try:
                        config.read(self.config_file)
                    except:
                        raise inquestlabs_exception("invalid configuration file: %s" % self.config_file)

                    try:
                        self.api_key = config.get("inquestlabs", "apikey")
                    except:
                        raise inquestlabs_exception("unable to find inquestlabs.apikey in: %s" % self.config_file)

                    # update the source, include the path.
                    self.api_key_source = "config: %s" % self.config_file

            # NOTE: if we still don't have an API key that's fine! InQuest Labs will simply work with some rate limits.
            self.__VERBOSE("api_key=%s" % self.api_key, DEBUG)
            self.__VERBOSE("api_key_source=%s" % self.api_key_source, INFO)

    ####################################################################################################################
    def API (self, api, data=None, path=None, method="GET", raw=False):
        """
        Internal API wrapper.

        :type  api:    str
        :param api:    API endpoint, appended to base URL.
        :type  data:   dict
        :param data:   Optional data dictionary to pass to endpoint.
        :type  path:   str
        :param path:   Optional path to file to pass to endpoint.
        :type  method: str
        :param method: API method, one of "GET" or "POST".
        :type  raw:    bool
        :param raw:    Default behavior is to expect JSON encoded content, raise this flag to expect raw data.

        :rtype:  dict | str
        :return: Response dictionary or string if 'raw' flag is raised.
        """

        assert method in ["GET", "POST"]

        # if a file path was supplied, convert to a dictionary compatible with requests and the labs API.
        files = None

        if path:
            files = dict(file=open(path, "rb"))

        # initialize headers with a custom user-agent and if an API key is available, add an authorization header.
        headers = \
        {
            "User-Agent" : "python-inquestlabs/%s" % __version__
        }

        if self.api_key:
            headers["Authorization"] = "Basic %s" % self.api_key

        # build the keyword arguments that will be passed to requests library.
        kwargs = \
        {
            "data"    : data,
            "files"   : files,
            "headers" : headers,
            "proxies" : self.proxies,
            "verify"  : self.verify_ssl,
        }

        # make attempts to dance with the API endpoint, use a jittered exponential back-off delay.
        last_exception = None
        endpoint       = self.base_url + api
        attempt        = 0

        self.__VERBOSE("%s %s" % (method, endpoint), INFO)

        while 1:
            try:
                response = requests.request(method, endpoint, **kwargs)
                self.api_requests_made += 1
                self.__VERBOSE("[%d] %s" % (self.api_requests_made, kwargs), DEBUG)
                break

            except Exception as e:
                last_exception = e
                self.__VERBOSE("API exception: %s" % e, INFO)

                # 0.4, 1.6, 6.4, 25.6, ...
                time.sleep(random.uniform(0, 4 ** attempt * 100 / 1000.0))
                attempt += 1

            # retries exhausted.
            if attempt == self.retries:
                message = "exceeded %s attempts to communicate with InQuest Labs API endpoint %s."
                message %= self.retries, endpoint

                if last_exception:
                    message += "\nlast exception:\n%s" % str(last_exception)

                raise inquestlabs_exception(message)

        # update internal rate limit tracking variables.
        if hasattr(response, "headers"):
            self.rlimit_requests_remaining = response.headers.get('X-RateLimit-Remaining')
            self.rlimit_reset_epoch_time   = response.headers.get('X-RateLimit-Reset')

            if self.rlimit_requests_remaining:
                self.rlimit_requests_remaining = int(self.rlimit_requests_remaining)

            if self.rlimit_reset_epoch_time:
                self.rlimit_reset_epoch_time  = int(self.rlimit_reset_epoch_time)
                self.rlimit_seconds_to_reset  = int(self.rlimit_reset_epoch_time - time.time())
                self.rlimit_reset_epoch_ctime = time.ctime(self.rlimit_reset_epoch_time)

        self.__VERBOSE("API status_code=%d" % response.status_code, INFO)
        self.__VERBOSE(response.content, DEBUG)

        # all good.
        if response.status_code == 200:

            # if the raw flag was raised, return raw content now.
            if raw:
                return response.content

            # otherwise, we convert the assumed JSON response to a python dictionary.
            response_json = response.json()

            # with a 200 status code, success should always be true...
            if response_json['success']:
                return response_json['data']

            # ... but let's handle corner cases where it may not be.
            else:
                message  = "status=200 but error communicating with %s: %s"
                message %= endpoint, response_json.get("error", "n/a")
                raise inquestlabs_exception(message)

        # rate limit exhaustion.
        elif response.status_code == 429:
            raise inquestlabs_exception("status=429 rate limit exhausted!")

        # something else went wrong.
        else:
            message  = "status=%d error communicating with %s: "
            message %= response.status_code, endpoint

            try:
                response_json = response.json()
                message += response_json.get("error", "n/a")
            except:
                message += str(response.content)

            raise inquestlabs_exception(message)

    ####################################################################################################################
    def __HASH (self, path=None, bytes=None, algorithm="md5", block_size=16384, fmt="digest"):
        """
        Return the selected algorithms crytographic hash hex digest of the given file.

        :type  path:       str
        :param path:       Path to file to hash or None if supplying bytes.
        :type  bytes:      str
        :param bytes:      str bytes to hash or None if supplying a path to a file.
        :type  algorithm:  str
        :param algorithm:  One of "md5", "sha1", "sha256" or "sha512".
        :type  block_size: int
        :param block_size: Size of blocks to process.
        :type  fmt:        str
        :param fmt:        One of "digest" (str), "raw" (hashlib object), "parts" (array of numeric parts).

        :rtype:  str
        :return: Hash as hex digest.
        """

        def chunks (l, n):
            for i in range(0, len(l), n):
                yield l[i:i+n]

        algorithm = algorithm.lower()

        if   algorithm == "md5":    hashfunc = hashlib.md5()
        elif algorithm == "sha1":   hashfunc = hashlib.sha1()
        elif algorithm == "sha256": hashfunc = hashlib.sha256()
        elif algorithm == "sha512": hashfunc = hashlib.sha512()

        # hash a file.
        if path:
            with open(path, "rb") as fh:
                while 1:
                    data = fh.read(block_size)

                    if not data:
                        break

                    hashfunc.update(data)

        # hash a stream of bytes.
        elif bytes:
            hashfunc.update(bytes)

        # error.
        else:
            raise inquestlabs_exception("hash expects either 'path' or 'bytes'.")

        # return multiplexor.
        if fmt == "raw":
            return hashfunc

        elif fmt == "parts":
            return map(lambda x: int(x, 16), list(chunks(hashfunc.hexdigest(), 8)))

        else: # digest
            return hashfunc.hexdigest()

    ####################################################################################################################
    def __HASH_VALIDATE (self, hash_str, length=None):
        """
        Determine if the given hash string contains valid hex chars for the specified length or entirely, if left out.

        :type  hash_str: str
        :param hash_str: Hash string to verify.
        :type  length:   int
        :param length:   Number of characters in hash string.

        :rtype:  bool
        :return: True is hash string is valid, False otherwise.
        """

        if not hash_str:
            return None

        if length and len(hash_str) != length:
            return False

        if re.match("[0-9a-fA-F]+", hash_str, re.I):
            return True

        return False

    ####################################################################################################################
    def __VERBOSE (self, message, verbosity=INFO):
        """
        Outputs 'message' to stderr if instance verbosity is equal to or greater than the supplied verbosity.

        :type  message:   str
        :param message:   Path to file to hash or None if supplying bytes.
        :type  verbosity: int
        :param verbosity: Minimum verbosity level required to display message.
        """

        if self.verbosity >= verbosity:
            sys.stderr.write("[verbosity=%d] %s\n" % (self.verbosity, message))

    ####################################################################################################################
    # hash shorcuts.
    def md5    (self, path=None, bytes=None): return self.__HASH(path=path, bytes=bytes, algorithm="md5")
    def sha1   (self, path=None, bytes=None): return self.__HASH(path=path, bytes=bytes, algorithm="sha1")
    def sha256 (self, path=None, bytes=None): return self.__HASH(path=path, bytes=bytes, algorithm="sha256")
    def sha512 (self, path=None, bytes=None): return self.__HASH(path=path, bytes=bytes, algorithm="sha512")

    def is_md5    (self, hash_str): return self.__HASH_VALIDATE(hash_str,  32)
    def is_sha1   (self, hash_str): return self.__HASH_VALIDATE(hash_str,  40)
    def is_sha256 (self, hash_str): return self.__HASH_VALIDATE(hash_str,  64)
    def is_sha512 (self, hash_str): return self.__HASH_VALIDATE(hash_str, 128)

    ####################################################################################################################
    def dfi_attributes (self, sha256, filter_by=None):
        """
        Retrieve attributes for a given file by SHA256 hash value.

        :type  sha256:  str
        :param sha256:  SHA256 hash for the file we are interested in.
        :type  filter_by: str
        :param filter_by: Optional filter, can be one of 'domain', 'email', 'filename', 'filepath', ip', 'registry', 'url', 'xmpid'.
        :rtype:  dict
        :return: API response.
        """

        # if a filter is specified, sanity check.
        if filter_by:
            filter_by = filter_by.lower()

            if filter_by not in VALID_IOC:
                message  = "invalid attribute filter '%s'. valid filters include: %s"
                message %= filter_by, ", ".join(VALID_IOC)
                raise inquestlabs_exception(message)

        # dance with the API.
        attributes = self.API("/dfi/details/attributes", dict(sha256=sha256))

        # filter if necessary.
        if filter_by:
            # sample data:
            #     [
            #       {
            #         "category": "ioc",
            #         "attribute": "domain",
            #         "count": 1,
            #         "value": "ancel.To"
            #       },
            #       {
            #         "category": "ioc",
            #         "attribute": "domain",
            #         "count": 1,
            #         "value": "Application.Top"
            #       }
            #     ]
            attributes = [attr for attr in attributes if attr['attribute'] == filter_by]

        # return attributes.
        return attributes

    ####################################################################################################################
    def dfi_details (self, sha256, attributes=False):
        """
        Retrieve details for a given file by SHA256 hash value. Optionally, pull attributes in a second API request
        and append to the data dictionary under the key 'attributes'.

        Returned dictionary keys and value types include::
            analysis_completed: bool
            classification: MALICIOUS|BENIGN
            ext_code: str
            ext_context: str
            ext_metadata: str
            ext_ocr: str
            file_type: CAB|DOC|DOCX|EML|MSI|OLE|PCAP|PPT|TNEF|XLS
            first_seen: str ex: Thu, 07 Nov 2019 21:26:53 GMT
            inquest_alerts: dict keys=category,description,reference,title
            inquest_dfi_size: int
            last_inquest_dfi: str
            last_inquest_featext: str
            last_updated: str
            len_code: int
            len_context: int
            len_metadata: int
            len_ocr: int
            md5: str
            mime_type: str
            sha1: str
            sha256: str
            sha512: str
            size: int
            subcategory: str
            subcategory_url: str
            virus_total: str

        :type  sha256:     str
        :param sha256:     SHA256 hash for the file we are interested in.
        :type  attributes: bool
        :param attributes: Raise this flag to includes 'attributes' subkey.

        :rtype:  dict
        :return: API response.
        """

        assert self.is_sha256(sha256)

        # API dance.

        data = self.API("/dfi/details", dict(sha256=sha256))


        if attributes:
            data['attributes'] = self.dfi_attributes(sha256)

        return data

    ####################################################################################################################
    def dfi_download (self, sha256, path, encrypt=False):
        """
        Download requested file and save to path.

        :type  sha256:  str
        :param sha256:  SHA256 hash for the file we are interested in.
        :type  path:    str
        :param path:    Where we want to save the file.
        :type  encrypt: bool
        :param encrypt: Raise this flag to download the file inside a Zip file encrypted with the password 'infected'.
        """

        assert self.is_sha256(sha256)

        # NOTE: we're reading the file directly into memory here! not worried about it as the files are small and we
        # done anticipate any OOM issues.
        data = self.API("/dfi/download", dict(sha256=sha256, encrypt_download=encrypt), raw=True)

        # if we requested a raw download, then ensure we got what we were looking for.
        if not encrypt:
            calculated = self.sha256(bytes=data)

            if calculated != sha256:
                message  = "failed downloading file! expected sha256=%s calculated sha256=%s"
                message %= sha256, calculated
                raise inquestlabs_exception(message)

        # write the file to disk.
        with open(path, "wb+") as fh:
            fh.write(data)

    ####################################################################################################################
    def dfi_list (self, malicious=None, kind=None, has_code=None, has_context=None, has_metadata=None, has_ocr=None):
        """
        Retrieve the most recent DFI entries. Example dictionary returned in list::

            {'analysis_completed': True,
             'classification': 'MALICIOUS',
             'file_type': 'DOC',
             'first_seen': 'Thu, 07 Nov 2019 21:26:53 GMT',
             'inquest_alerts': [],
             'last_inquest_featext': 'Thu, 07 Nov 2019 21:30:23 GMT',
             'len_code': 10963,
             'len_context': 24,
             'len_metadata': 1021,
             'len_ocr': 0,
             'mime_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
             'sha256': 'f7702e873c1a26e8171d771180108a9735cb5a2b69958e14b51eb572973cfb7b',
             'size': 821038,
             'subcategory': 'macro_hunter',
             'subcategory_url': 'https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule'}

        :type  malicious:    bool
        :param malicious:    Filter results by whether or not they are malicious.
        :type  kind:         str
        :param kind:         Filter list by high level type, ex: 'DOC', 'DOCX', 'OLE', 'PPT', 'XLS'.
        :type  has_code:     int
        :param has_code:     Filter results by whether or not they contain X bytes of embedded logic.
        :type  has_context:  int
        :param has_context:  Filter results by whether or not they contain X bytes of semantic information.
        :type  has_metadata: int
        :param has_metadata: Filter results by whether or not they contain X bytes of any metadata.
        :type  has_ocr:      int
        :param has_ocr:      Filter results by whether or not they contain X bytes of OCR extracted semantic data.

        :rtype:  list
        :return: List of dictionaries.
        """

        filtered = []

        for entry in self.API("/dfi/list"):


            # process filters as disqualifiers.
            if malicious == True and entry['classification'] != "MALICIOUS":
                continue

            if malicious == False and entry['classification'] != "UNKNOWN":
                continue

            if kind is not None and entry['file_type'] != kind:
                continue

            if has_code is not None and entry['len_code'] < has_code:
                continue

            if has_context is not None and entry['len_context'] < has_context:
                continue

            if has_metadata is not None and entry['len_metadata'] < has_metadata:
                continue

            if has_ocr is not None and entry['len_ocr'] < has_ocr:
                continue

            # if we're still here, we keep the entry.
            filtered.append(entry)

        return filtered

    ####################################################################################################################
    def dfi_search (self, category, subcategory, keyword):
        """
        Search DFI category/subcategory by keyword. Valid categories include: 'ext', 'hash', and 'ioc'. Valid
        subcategories for each include: ext: 'code', 'context', 'metadata', and 'ocr'. hash: 'md5', 'sha1', 'sha256',
        and 'sha512'. ioc: 'domain', 'email', 'filename', 'filepath', ip', 'registry', url', 'xmpid'. See
        https://labs.inquest.net for more information.

        Example dictionary returned in list of matched entries::

            {'analysis_completed': True,
             'classification': 'MALICIOUS',
             'file_type': 'DOC',
             'first_seen': 'Thu, 07 Nov 2019 21:26:53 GMT',
             'inquest_alerts': [],
             'last_inquest_featext': 'Thu, 07 Nov 2019 21:30:23 GMT',
             'len_code': 10963,
             'len_context': 24,
             'len_metadata': 1021,
             'len_ocr': 0,
             'mime_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
             'sha256': 'f7702e873c1a26e8171d771180108a9735cb5a2b69958e14b51eb572973cfb7b',
             'size': 821038,
             'subcategory': 'macro_hunter',
             'subcategory_url': 'https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule'}

        :type  category:    str
        :param category:    Search category, one of 'ext', 'hash', or 'ioc'.
        :type  subcategory: str
        :param subcategory: Search subcategory.
        :type  keyword:     str
        :param keyword:     Keyword, hash, or IOC to search for.

        :rtype:  list
        :return: API response.
        """

        # normalize to lowercase.
        category    = category.lower()
        subcategory = subcategory.lower()

        # sanity check.
        if category not in VALID_CAT:
            message  = "invalid category '%s'. valid categories include: %s"
            message %= category, ", ".join(VALID_CAT)
            raise inquestlabs_exception(message)

        for c, v in zip(VALID_CAT, [VALID_EXT, VALID_HASH, VALID_IOC]):
            if category == c and subcategory not in v:
                message  = "invalid subcategory '%s' for category '%s'. valid subcategories include: %s"
                message %= subcategory, category, ", ".join(v)
                raise inquestlabs_exception(message)

        # API dance.
        if category == "ext":
            subcategory = "ext_" + subcategory

        if category == "hash":
            data = dict(hash=keyword)
        else:
            data = dict(keyword=keyword)

        return self.API("/dfi/search/%s/%s" % (category, subcategory), data)

    ####################################################################################################################
    def dfi_sources (self):
        """
        Retrieves the list of YARA hunt rules that run atop of Virus Total Intelligence and fuel the majority of the
        DFI corpus.

        :rtype:  dict
        :return: API response.
        """

        return self.API("/dfi/sources")

    ####################################################################################################################
    def dfi_upload (self, path):
        """
        Uploads a file to InQuest Labs for Deep File Inspection (DFI). Note that the file must be one of doc, docx, ppt,
        pptx, xls, xlsx.

        :type  path: str
        :param path: Path to file to upload.

        :rtype:  dict
        :return: API response.
        """

        VALID_TYPES = ["doc", "docx", "ppt", "pptx", "xls", "xlsx"]

        # ensure the path exists and points to a file.
        if not os.path.exists(path) or not os.path.isfile(path):
            raise inquestlabs_exception("invalid file path specified for upload: %s" % path)

        # ensure the file is an OLE (pre 2007 Office file) or ZIP (post 2007 Office file).
        with open(path, "rb") as fh:
            if fh.read()[:2] not in [b"\xD0\xCF", b"PK"]:
                message  = "unsupported file type for upload, valid files include: %s, etc..."
                message %= ", ".join(VALID_TYPES)
                raise inquestlabs_exception(message)

        # dance with the API.
        return self.API("/dfi/upload", method="POST", path=path)

    ####################################################################################################################
    def iocdb_list (self, kind=None, ref_link_keyword=None, ref_text_keyword=None):
        """
        Retrieve a list of the most recent entries added to the InQuest Labs IOC database. Example data::

            {
              "artifact": "85b936960fbe5100c170b777e1647ce9f0f01e3ab9742dfc23f37cb0825b30b5",
              "artifact_type": "hash",
              "created_date": "Thu, 14 Nov 2019 19:14:55 GMT",
              "reference_link": "http://feedproxy.google.com/~r/feedburner/Talos/~3/cWpezcI4rFw/threat-source-newsletter-nov-14-2019.html",
              "reference_text": "Newsletter compiled by Jon Munshaw. Welcome to this week's Threat Source newsletter - the perfect place to get caught up on all things Talos..."
            }

        :type  kind:             str
        :param kind:             Filter results by data type, can be one of 'ip', 'url', 'domain', 'yara', 'hash'.
        :type  ref_link_keyword: str
        :param ref_link_keyword: Filter results by keyword in reference link.
        :type  ref_text_keyword: str
        :param ref_text_keyword: Filter results by keyword in reference text.

        :rtype:  dict
        :return: API response.
        """

        filtered = []

        for entry in self.API("/iocdb/list"):

            # process filters as disqualifiers.
            if kind is not None and not entry['artifact_type'].startswith(kind.lower()):
                continue

            if ref_link_keyword is not None and ref_link_keyword not in entry['reference_link'].lower():
                continue

            if ref_text_keyword is not None and ref_text_keyword not in entry['reference_text'].lower():
                continue

            # if we're still here, we keep the entry.
            filtered.append(entry)

        return filtered

    ####################################################################################################################
    def iocdb_search (self, keyword):
        """
        Search the InQuest Labs IOC database for entries matching the keyword.

        :type  keyword: str
        :param keyword: Search term.

        :rtype:  dict
        :return: API response.
        """

        return self.API("/iocdb/search", dict(keyword=keyword))

    ####################################################################################################################
    def iocdb_sources (self):
        """
        Retrieves the list of sources that fuel the InQuest Labs IOC database.

        :rtype:  dict
        :return: API response.
        """

        return self.API("/iocdb/sources")

    ########################################################################################################################
    def is_ipv4 (self, s):
        # we prefer to use the ipaddress third-party module here, but fall back to a regex solution.
        try:
            import ipaddress
        except:
            if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", s):
                return True
            else:
                return False

        # python 2/3 compat
        try:
            s = unicode(s)
        except:
            pass

        # is instance of IPv4 address?
        try:
            return isinstance(ipaddress.ip_address(s), ipaddress.IPv4Address)
        except:
            return False


    ########################################################################################################################
    def is_ipv6 (self, s):
        # best effort pull in third-party module.
        try:
            import ipaddress
        except:
            return None

        # python 2/3 compat
        try:
            s = unicode(s)
        except:
            pass

        # is instance of IPv6 address?
        try:
            return isinstance(ipaddress.ip_address(s), ipaddress.IPv6Address)
        except:
            return False


    ####################################################################################################################
    def is_domain (self, s):
        return VALID_DOMAIN.match(s)

    ####################################################################################################################
    def is_ip (self, s):
        return self.is_ipv4(s) or self.is_ipv6(s)

    ####################################################################################################################
    def lookup (self, kind, ioc):
        """
        Lookup information regarding IP address or Domain Name.

        :type  kind: str
        :param kind: One of "IP" or "Domain".
        :type  ioc:  str
        :param ioc:  Indicator to lookup.

        :rtype:  dict
        :return: API response.
        """

        kind = kind.lower()
        assert kind in ["ip", "domain"]

        return self.API("/lookup/%s" % kind, dict(indicator=ioc))

    ####################################################################################################################
    def rate_limit_banner (self):
        """
        Returns a string describing number of API requests made since instantiation, remaining API credits (if a rate
        limit is imposed), and when the rate limit window resets.

        :rtype:  str
        :return: Request and rate limit information, in human readable format.
        """

        if not self.api_requests_made:
            return "Rate limit information not available, no API requests made."

        if self.rlimit_requests_remaining:
            limit_banner  = "%d API requests made. %d API requests remaining. Rate limit window resets on %s."
            limit_banner %= self.api_requests_made, self.rlimit_requests_remaining, self.rlimit_reset_epoch_ctime
        else:
            limit_banner  = "%d API requests made. No rate limit! API key sourced from %s."
            limit_banner %= self.api_requests_made, self.api_key_source

        return limit_banner

    ####################################################################################################################
    def repdb_list (self, kind=None, source=None):
        """
        Retrieve a list of the most recent entries added to the InQuest Labs reputation database. Example data::

            {
              "created_date": "Thu, 14 Nov 2019 18:22:00 GMT",
              "data": "beautyevent.ru/Invoice-for-j/b-03/05/2018/",
              "data_type": "url",
              "derived": "beautyevent.ru",
              "derived_type": "domain",
              "source": "urlhaus",
              "source_url": "https://urlhaus.abuse.ch/host/beautyevent.ru"
            }

        :type  kind:   str
        :param kind:   Filter results by data type, can be one of 'ip', 'url', 'domain', 'asn'.
        :type  source: str
        :param source: Filter results by source, examples include: 'alienvault', 'blocklist', 'urlhaus', etc..

        :rtype:  dict
        :return: API response.
        """

        filtered = []

        for entry in self.API("/repdb/list"):

            # process filters as disqualifiers.
            if kind is not None and not entry['data_type'].startswith(kind.lower()):
                continue

            if source is not None and not entry['source'].startswith(source.lower()):
                continue

            # if we're still here, we keep the entry.
            filtered.append(entry)

        return filtered

    ####################################################################################################################
    def repdb_search (self, keyword):
        """
        Search the InQuest Labs reputation database for entries matching the keyword.

        :type  keyword: str
        :param keyword: Search term.

        :rtype:  dict
        :return: API response.
        """

        return self.API("/repdb/search", dict(keyword=keyword))

    ####################################################################################################################
    def repdb_sources (self):
        """
        Retrieves the list of sources that fuel the InQuest Labs reputaiton database.

        :rtype:  dict
        :return: API response.
        """

        return self.API("/repdb/sources")

    ####################################################################################################################
    def report (self, ioc, timeout=None):
        """
        Leverage multiprocessing to produce a single report for the supplied IP/domain indicator which includes data
        from: lookup, DFIdb, REPdb, and IOCdb.

        :type  ioc:     str
        :param ioc:     Indicator to lookup (IP, domain, URL)
        :type timeout:  integer
        :param timeout: Maximum time given to producing the IOC report (default=60).

        :rtype:  dict
        :return: API response.
        """

        # default timeout.
        if timeout is None:
            timeout = 60

        # parallelization.
        jobs = []
        mngr = multiprocessing.Manager()
        resp = mngr.dict()

        # what kind of IOC are we dealing with.
        if self.is_ip(ioc):
            kind = "ip"
        elif self.is_domain(ioc):
            kind = "domain"
        elif ioc.startswith("http"):
            kind = "url"
        else:
            raise inquestlabs_exception("could not determine indicator type for %s" % ioc)

        # only IPs and domains get lookups.
        if kind in ["ip", "domain"]:
            job = multiprocessing.Process(target=worker_proxy, args=(self, "lookup", [kind, ioc], resp))
            jobs.append(job)
            job.start()

        # all IOCs get compared against DFIdb, REPdb, and IOCdb
        job = multiprocessing.Process(target=worker_proxy, args=(self, "dfi_search", ["ioc", kind, ioc], resp))
        jobs.append(job)
        job.start()

        job = multiprocessing.Process(target=worker_proxy, args=(self, "repdb_search", [ioc], resp))
        jobs.append(job)
        job.start()

        job = multiprocessing.Process(target=worker_proxy, args=(self, "iocdb_search", [ioc], resp))
        jobs.append(job)
        job.start()

        # wait for jobs to complete.
        self.__VERBOSE("waiting up to %d seconds for %d jobs to complete" % (timeout, len(jobs)))

        # wait for jobs to complete, up to timeout
        start = time.time()

        while time.time() - start <= timeout:
            if not any(job.is_alive() for job in jobs):
                # all the processes are done, break now.
                break

            # this prevents CPU hogging.
            time.sleep(1)

        else:
            self.__VERBOSE("timeout reached, killing jobs...")
            for job in jobs:
                job.terminate()
                job.join()

        elapsed = time.time() - start
        self.__VERBOSE("completed all jobs in %d seconds" % elapsed)

        # return the combined response.
        return dict(resp)


    ####################################################################################################################
    def stats (self):
        """
        Retrieve statistics from InQuest Labs.

        :rtype:  list
        :return: List of dictionaries.
        """

        return self.API("/stats")

    ####################################################################################################################
    def trystero_list_days (self):
        """
        Retrieve the list of days and sample counts that we have Trystero data on. For further information on Trystero,
        see https://labs.inquest.net/trystero for further information. Example data::

            {
              "2021-08-04": 406,
              "2021-08-05": 30,
              "2021-08-06": 49,
              "2021-08-07": 30,
              "2021-08-09": 22,
              "2021-08-10": 36,
              "first_record": "2020-08-09"
            }

        :rtype:  dict
        :return: Dictionary of key=date value=count pairs.
        """

        return self.API("/trystero/list")

    ####################################################################################################################
    def trystero_list_samples (self, date):
        """
        Retrieve the list of samples from the Trysteo project (these are samples that bypassed either Microsoft, Google,
        or both. For further information on Trystero, see https://labs.inquest.net/trystero. Example data::

            [
              {
                "analysis_completed": false,
                "available_on_labs": false,
                "bypasses": "microsoft",
                "classification": "MALICIOUS",
                "downloadable": false,
                "file_type": "OTHER",
                "first_seen": "2021-08-09T23:16:46",
                "image": false,
                "inquest_alerts": [
                  {
                    "category": "info",
                    "description": "Found a Windows Portable Executable (PE) binary. Depending on context, the presence of a binary is suspicious or malicious.",
                    "reference": null,
                    "title": "Windows PE Executable"
                  }
                ],
                "last_inquest_featext": null,
                "mime_type": "application/x-msi",
                "sha256": "01241e05ebab5c9f010de24dd3e611a4eb5b4ad883bafbb416383195bb423182",
                "size": 14752768,
                "subcategory": "maldoc_hunter",
                "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maldoc_hunter.rule",
                "vt_positives": 4,
                "vt_weight": 2.799999952316284
              }
            ]

        :type date:  str
        :param date: Date for which we wish to retrieve sample information.

        :rtype:  list
        :return: List of dictionaries.
        """

        return self.API("/trystero/%s" % date)

    ####################################################################################################################
    def yara_b64re (self, regex, endian=None):
        """
        Save time and avoid tedious manual labor by automatically converting plain-text regular expressions into their
        base64 compatible form.

        :type  regex:  str
        :param regex:  Regular expression to convert.
        :type  endian: str
        :param endian: Optional endianess, can be either "BIG" or "LITTLE".

        :rtype:  str
        :return: Base64 matching regular expression.
        """

        # initialize data dictionary with supplied regular expression.
        data = dict(instring=regex)

        # splice in the appropriate endianess option if supplied.
        if endian:
            endian = endian.upper()

            if endian == "BIG":
                data['option'] = "widen_big"
            elif endian == "LITTLE":
                data['option'] = "widen_little"
            else:
                raise inquestlabs_exception("invalid endianess supplied to yara_b64re: %s" % endian)

        # dance with the API and return results.
        return self.API("/yara/base64re", data)

    ####################################################################################################################
    def yara_hexcase (self, instring):
        """
        Translate hex encoded strings into a regular expression form that is agnostic to MixED CaSE CharACtErS.

        :type  instring: str
        :param instring: String to convert.

        :rtype:  str
        :return: Mixed hex case insensitive regular expression.
        """

        return self.API("/yara/mixcase", dict(instring=instring))

    ####################################################################################################################
    def yara_widere (self, regex, endian=None):
        """
        Save time and avoid tedious manual labor by automating converting ascii regular expressions widechar forms.

        :type  regex:  str
        :param regex:  Regular expression to convert.
        :type  endian: str
        :param endian: Optional endianess, can be either "BIG" or "LITTLE".

        :rtype:  str
        :return: Widened regular expression.
        """

        # initialize data dictionary with supplied regular expression.
        data = dict(instring=regex)

        # splice in the appropriate endianess option if supplied.
        if endian:
            endian = endian.upper()

            if endian in ["BIG", "LITTLE"]:
                data['kind'] = endian
            else:
                raise inquestlabs_exception("invalid endianess supplied to yara_b64re: %s" % endian)

        # dance with the API and return results.
        return self.API("/yara/widere", data)

    ####################################################################################################################
    def yara_uint (self, magic, offset=0, is_hex=False):
        """
        Improve the performance of your YARA rules by converting string comparisons into unsigned integer pointer
        dereferences.

        :type  magic:  str
        :param magic:  String we which to convert to unit() trigger.
        :type  offset: int
        :param offset: Optional offset in hex (0xde) or decimal (222) to look for magic at, defaults to 0.
        :type  hex:    bool
        :param hex:    Raise this flag to treat 'magic' as hex encoded bytes.

        :rtype:  str
        :return: YARA condition looking for magic at offset via uint() magic.
        """

        return self.API("/yara/trigger", dict(trigger=magic, offset=offset, is_hex=is_hex))

########################################################################################################################
########################################################################################################################
########################################################################################################################

def main ():
    args = docopt.docopt(__doc__, version=__version__)

    # --debug is for docopt argument parsing. useful to pipe to: egrep -v "False|None"
    if args['--debug']:
        print(args)
        return

    # instantiate interface to InQuest Labs.
    labs = inquestlabs_api(args['--api'], args['--config'], args['--proxy'], verbose=int(args['--verbose']))

    ### DFI ############################################################################################################
    if args['dfi']:

        # inquestlabs [options] dfi attributes <sha256> [--filter=<filter>]
        if args['attributes']:
            print(json.dumps(labs.dfi_attributes(args['<sha256>'], args['--filter'])))

        # inquestlabs [options] dfi details <sha256> [--attributes]
        elif args['details']:
            print(json.dumps(labs.dfi_details(args['<sha256>'], args['--attributes'])))

        # inquestlabs [options] dfi download <sha256> <path> [--encrypt]
        elif args['download']:
            start = time.time()
            labs.dfi_download(args['<sha256>'], args['<path>'], args['--encrypt'])
            print("saved %s as '%s' in %d seconds." % (args['<sha256>'], args['<path>'], time.time() - start))

        # inquestlabs [options] dfi list
        elif args['list']:
            print(json.dumps(labs.dfi_list()))

        elif args['search']:

            # inquestlabs [options] dfi search (code|context|metadata|ocr) <keyword>
            if args['<keyword>']:
                if args['code']:
                    results = labs.dfi_search("ext", "code", args['<keyword>'])
                elif args['context']:
                    results = labs.dfi_search("ext", "context", args['<keyword>'])
                elif args['metadata']:
                    results = labs.dfi_search("ext", "metadata", args['<keyword>'])
                elif args['ocr']:
                    results = labs.dfi_search("ext", "ocr", args['<keyword>'])
                else:
                    raise inquestlabs_exception("keyword search argument parsing fail.")

            # inquestlabs [options] dfi search (md5|sha1|sha256|sha512) <hash>
            elif args['<hash>']:
                if args['md5']:
                    results = labs.dfi_search("hash", "md5", args['<hash>'])
                elif args['sha1']:
                    results = labs.dfi_search("hash", "sha1", args['<hash>'])
                elif args['sha256']:
                    results = labs.dfi_search("hash", "sha256", args['<hash>'])
                elif args['sha512']:
                    results = labs.dfi_search("hash", "sha512", args['<hash>'])
                else:
                    raise inquestlabs_exception("hash search argument parsing fail.")

            # inquestlabs [options] dfi search (domain|email|filename|filepath|ip|registry|url|xmpid) <ioc>
            elif args['<ioc>']:
                if args['domain']:
                    results = labs.dfi_search("ioc", "domain", args['<ioc>'])
                elif args['email']:
                    results = labs.dfi_search("ioc", "email", args['<ioc>'])
                elif args['filename']:
                    results = labs.dfi_search("ioc", "filename", args['<ioc>'])
                elif args['filepath']:
                    results = labs.dfi_search("ioc", "filepath", args['<ioc>'])
                elif args['ip']:
                    results = labs.dfi_search("ioc", "ip", args['<ioc>'])
                elif args['registry']:
                    results = labs.dfi_search("ioc", "registry", args['<ioc>'])
                elif args['url']:
                    results = labs.dfi_search("ioc", "url", args['<ioc>'])
                elif args['xmpid']:
                    results = labs.dfi_search("ioc", "xmpid", args['<ioc>'])
                else:
                    raise inquestlabs_exception("ioc search argument parsing fail.")

            # search results.
            print(json.dumps(results))

        # inquestlabs [options] dfi sources
        elif args['sources']:
            print(json.dumps(labs.dfi_sources()))

        # inquestlabs [options] dfi upload <path>
        elif args['upload']:
            start  = time.time()
            sha256 = labs.dfi_upload(args['<path>'])
            print("successfully uploaded %s in %d seconds." % (args['<path>'], time.time() - start))
            print("see results at: https://labs.inquest.net/dfi/sha256/%s" % sha256)

        # huh?
        else:
            raise inquestlabs_exception("dfi argument parsing fail.")

    ### IOCDB ##########################################################################################################
    elif args['iocdb']:

        # inquestlabs [options] iocdb list
        if args['list']:
            print(json.dumps(labs.iocdb_list()))

        # inquestlabs [options] iocdb search <keyword>
        elif args['search']:
            print(json.dumps(labs.iocdb_search(args['<keyword>'])))

        # inquestlabs [options] iocdb sources
        elif args['sources']:
            print(json.dumps(labs.iocdb_sources()))

        # huh?
        else:
            raise inquestlabs_exception("iocdb argument parsing fail.")

    ### REPDB ##########################################################################################################
    elif args['repdb']:

        # inquestlabs [options] repdb list
        if args['list']:
            print(json.dumps(labs.repdb_list()))

        # inquestlabs [options] repdb search <keyword>
        elif args['search']:
            print(json.dumps(labs.repdb_search(args['<keyword>'])))

        # inquestlabs [options] repdb sources
        elif args['sources']:
            print(json.dumps(labs.repdb_sources()))

        # huh?
        else:
            raise inquestlabs_exception("repdb argument parsing fail.")

    ### YARA ###########################################################################################################
    elif args['yara']:

        # normalize big/little endian switches.
        if args['--big-endian']:
            endian = "BIG"
        elif args['--little-endian']:
            endian = "LITTLE"
        else:
            endian = None

        # NOTE: we don't json.dumps() these values as they are likely going to be wanted to be used raw and not piped
        #       into another JSON expectant tool.

        # inquestlabs [options] yara (b64re|base64re) <regex> [(--big-endian|--little-endian)]
        if args['b64re'] or args['base64re']:
            print(labs.yara_b64re(args['<regex>'], endian))

        # inquestlabs [options] yara hexcase <instring>
        elif args['hexcase']:
            print(labs.yara_hexcase(args['<instring>']))

        # inquestlabs [options] yara uint <instring> [--offset=<offset>] [--hex]
        elif args['uint']:
            print(labs.yara_uint(args['<instring>'], args['--offset'], args['--hex']))

        # inquestlabs [options] yara widere <regex> [(--big-endian|--little-endian)]
        elif args['widere']:
            print(labs.yara_widere(args['<regex>'], endian))

        # huh?
        else:
            raise inquestlabs_exception("yara argument parsing fail.")

    ### IP/DOMAIN LOOKUP ###############################################################################################
    elif args['lookup']:
        if args['ip']:
            print(json.dumps(labs.lookup('ip', args['<ioc>'])))

        elif args['domain']:
            print(json.dumps(labs.lookup('domain', args['<ioc>'])))

        else:
            raise inquestlabs_exception("'lookup' supports 'ip' and 'domain'.")

    ### IP/DOMAIN/URL REPORT ###########################################################################################
    elif args['report']:
        print(json.dumps(labs.report(args['<ioc>'], args['--timeout'])))

    ### MISCELLANEOUS ##################################################################################################
    elif args['stats']:
        print(json.dumps(labs.stats()))

    elif args['setup']:
        if os.path.exists(labs.config_file):
            print("config file already exists: %s, won't overwrite." % labs.config_file)
        else:
            try:
                with open(labs.config_file, "w+") as fh:
                    fh.write("[inquestlabs]\n")
                    fh.write("apikey: %s\n" % args['<apikey>'])
                print("config file at %s initialized with API key %s" % (labs.config_file, args['<apikey>']))
            except:
                print("failed writing apikey to config file: %s" % labs.config_file)

    ### TRYSTERO PROJECT DATA ##########################################################################################
    elif args['trystero']:

        # inquestlabs [options] trystero list-days
        if args['list-days']:
            print(json.dumps(labs.trystero_list_days()))

        # inquestlabs [options] trystero list-samples <yyyy-mm-dd>
        elif args['list-samples']:
            date = args['<yyyy-mm-dd>']

            if re.match("\d{4}-\d{2}-\d{2}", date):
                print(json.dumps(labs.trystero_list_samples(date)))
            else:
                raise inquestlabs_exception("invalidate date format: '%s', expecting ex: '2021-08-09'" % date)

        # huh?
        else:
            raise inquestlabs_exception("trystero argument parsing fail.")

    # huh?
    else:
        raise inquestlabs_exception("argument parsing fail.")

    ### WRAP UP ########################################################################################################
    if args['--limits']:
        sys.stderr.write(labs.rate_limit_banner() + "\n")

########################################################################################################################
if __name__ == '__main__':
    main()
