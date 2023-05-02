![Build Status](https://github.com/InQuest/python-inquestlabs/workflows/tests/badge.svg?branch=master)
![Developed by InQuest](https://inquest.net/images/inquest-badge.svg)
![PyPI Version](http://img.shields.io/pypi/v/inquestlabs.svg)

# inquestlabs
A Pythonic interface and command line tool for interacting with the
[InQuest Labs](https://labs.inquest.net) API. Note that an API key is *not* required to interact with this API. An API key does provide the ability to increase their lookback, remove rate limitations, and download available samples. Users can sign in via OAuth to generate API keys. There is no cost to sign in. Authentication is supported via LinkedIn, Twitter, Google, and Github.

Searchable API documentation with multi-language snippets: <https://labs.inquest.net/docs/>

OpenAPI (Swagger) specification: <https://app.swaggerhub.com/apis-docs/InQuest.net/InQuestLabs/1.0>

## Installation
The recommended way to install InQuest Labs API CLI is by using [pipx](https://pypa.github.io/pipx/). This installs the package and all dependencies in an isolated virtual environment that can be invoked easily.

```bash
pipx install inquestlabs
```

Alternately, or in cases where you want to use inquestlabs as a library,
you can install it using [pip](https://pip.pypa.io/).

```bash
pip install inquestlabs
```

## InQuest Labs Command Line Driver
To see the available command line tools and options, see the output of `inquestlabs --help`. It'll look something like this:

<details>
<summary>View example</summary>

```bash
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
```

</details>
<br />

## InQuest Labs API Integrations

The following third-party projects integrate with InQuest Labs:

* [MalOverview](https://github.com/alexandreborges/malwoverview) from
  [@ale_sp_brazil](https://twitter.com/ale_sp_brazil).
* [EML Analyzer](https://eml-analyzer.herokuapp.com/) from
  [@ninoseki](https://twitter.com/ninoseki).
* ["Spoken" IOCs](https://github.com/safernandez666/IOC) from
  [@safernandez666](https://twitter.com/safernandez666).
* [Axial R4PTOR](https://ax1al.com/projects/r4pt0r) from
  [@AXI4L](https://twitter.com/AXI4L).

Get in touch or issue a pull request to get your project listed.

## The Trystero Project

The vast majority of attacks (>90%) are email-borne. The "Trystero Project" is our code name for an experiment that we're actively conducting to measure the security efficacy of the two largest mail providers, Google and Microsoft, against real-world emerging malware. The basic idea is this... let's take real-world threats daily and loop it through the two most popular cloud email providers, Google and Microsoft. We'll monitor which samples make it to the inbox and compare the results over the time. You can read more, view graphs, explore data, and compare results at [InQuest Labs: Trystero Project](https://labs.inquest.net/trystero). If you're curious to explore the testing corpus further, see the following two command line options:

### List Trystero Days

For a list of days we have ran the Trystero Project and the number of samples harvested for each day. Note that `first_record` denotes the earliest record (2020-08-09).

<details>
<summary>View example</summary>

```bash
$ inquestlabs trystero list-days | jq .
{
  "2021-01-08": 27,
  "2021-01-09": 26,
  "2021-04-20": 47,
  "2020-12-31": 304,
  "2021-01-03": 21,
  "2021-01-01": 7,
  "2021-01-06": 35,
  "2021-01-07": 17,
  "2021-01-04": 17,
  "2021-01-05": 20,
  "2021-06-14": 8,
  "2021-07-27": 55,
  "2021-03-28": 17,
  "2021-03-29": 18,
  "2021-03-26": 269,
  "2021-03-27": 52,
  "2021-03-24": 169,
  "2021-03-25": 543,
  "2021-03-22": 5,
  "2021-03-23": 197,
  "2021-03-20": 28,
  "2021-03-21": 46,
  "2021-04-12": 5,
  "2021-04-13": 23,
  "2021-03-18": 142,
  "2021-04-11": 13,
  "2021-04-16": 28,
  "2021-04-17": 94,
  "2021-04-14": 30,
  "2021-04-15": 46,
  "2021-06-21": 9,
  "2021-04-18": 13,
  "2021-04-19": 16,
  "2021-04-07": 40,
  "2021-06-20": 33,
  "2021-07-11": 22,
  "2021-08-09": 22,
  "first_record": "2020-08-09",
  "2021-06-22": 23,
  "2021-05-20": 490,
  "2021-01-19": 139,
  "2021-01-18": 16,
  "2021-04-26": 11,
  "2020-12-20": 3,
  "2020-12-23": 124,
  "2021-05-07": 60,
  "2021-01-11": 42,
  "2021-01-10": 5,
  "2021-01-13": 4,
  "2021-01-15": 35,
  "2021-01-14": 115,
  "2021-01-17": 15,
  "2021-01-16": 26,
  "2021-07-10": 43,
  "2021-04-02": 117,
  "2021-06-24": 88,
  "2021-06-25": 67,
  "2021-04-05": 16,
  "2021-05-21": 741,
  "2021-06-26": 4,
  "2021-03-31": 54,
  "2021-03-30": 51,
  "2021-06-23": 48,
  "2021-04-04": 18,
  "2021-02-21": 9,
  "2021-02-20": 113,
  "2021-02-23": 47,
  "2021-02-22": 10,
  "2021-02-25": 235,
  "2021-02-24": 54,
  "2021-02-27": 39,
  "2021-02-26": 42,
  "2021-04-09": 15,
  "2021-02-28": 19,
  "2021-04-06": 32,
  "2021-07-22": 147,
  "2021-04-08": 42,
  "2021-05-22": 1314,
  "2021-04-24": 35,
  "2021-05-02": 22,
  "2021-01-28": 60,
  "2021-01-29": 183,
  "2020-11-06": 1,
  "2021-01-25": 19,
  "2021-01-26": 42,
  "2020-11-05": 2,
  "2021-01-20": 1168,
  "2020-11-03": 26,
  "2021-01-22": 516,
  "2021-01-23": 361,
  "2021-03-01": 12,
  "2021-03-02": 117,
  "2021-03-03": 31,
  "2021-03-04": 17,
  "2021-03-05": 11,
  "2021-03-06": 10,
  "2021-03-07": 9,
  "2021-03-08": 13,
  "2021-03-09": 19,
  "2021-04-03": 45,
  "2021-05-03": 7,
  "2021-02-14": 5,
  "2021-02-15": 8,
  "2021-02-16": 19,
  "2021-02-17": 426,
  "2021-02-10": 113,
  "2021-02-11": 107,
  "2021-02-12": 77,
  "2021-02-13": 67,
  "2021-02-18": 40,
  "2021-02-19": 121,
  "2021-05-24": 20,
  "2021-06-30": 64,
  "2021-08-05": 30,
  "2021-08-04": 406,
  "2021-08-07": 30,
  "2021-08-06": 49,
  "2021-08-01": 582,
  "2021-08-03": 154,
  "2021-08-02": 60,
  "2021-07-13": 17,
  "2021-01-31": 19,
  "2021-01-30": 144,
  "2021-05-05": 95,
  "2021-07-12": 174,
  "2020-11-15": 1,
  "2021-04-10": 24,
  "2021-03-17": 113,
  "2021-03-16": 92,
  "2021-02-09": 389,
  "2021-02-08": 26,
  "2021-03-13": 197,
  "2021-03-12": 147,
  "2020-08-28": 1,
  "2021-03-10": 595,
  "2021-02-03": 87,
  "2021-02-02": 48,
  "2021-02-01": 13,
  "2020-08-25": 26,
  "2021-02-07": 33,
  "2021-02-06": 27,
  "2021-02-05": 103,
  "2021-02-04": 141,
  "2021-05-28": 33,
  "2021-07-15": 51,
  "2021-06-06": 154,
  "2021-06-09": 33,
  "2021-07-14": 43,
  "2021-03-15": 26,
  "2021-06-08": 33,
  "2020-12-18": 55,
  "2020-12-19": 14,
  "2021-03-14": 26,
  "2021-08-10": 36,
  "2021-04-29": 122,
  "2020-12-11": 1,
  "2020-12-15": 4,
  "2020-12-16": 18,
  "2020-12-17": 22,
  "2021-05-19": 180,
  "2021-03-11": 168,
  "2020-11-26": 1,
  "2021-07-16": 16,
  "2021-05-27": 236,
  "2020-08-26": 22,
  "2021-05-06": 71,
  "2021-04-28": 51,
  "2020-08-27": 7,
  "2020-08-31": 1,
  "2020-08-24": 5,
  "2021-05-31": 16,
  "2021-05-30": 11,
  "2021-05-18": 242,
  "2020-09-22": 1,
  "2020-09-25": 1,
  "2020-09-26": 1,
  "2020-08-22": 63,
  "2021-06-07": 22,
  "2021-05-01": 20,
  "2020-08-23": 2,
  "2021-01-24": 35,
  "2021-06-27": 2,
  "2020-08-20": 26,
  "2020-12-07": 1,
  "2020-12-05": 6,
  "2020-12-04": 4,
  "2020-12-03": 3,
  "2021-01-27": 99,
  "2021-01-21": 73,
  "2021-07-09": 30,
  "2021-04-27": 35,
  "2021-07-29": 184,
  "2021-06-11": 30,
  "2021-05-26": 27,
  "2021-07-23": 54,
  "2021-07-20": 5,
  "2021-07-26": 17,
  "2021-06-12": 26,
  "2021-07-24": 7,
  "2021-07-04": 8,
  "2021-06-13": 9,
  "2021-05-23": 31,
  "2021-04-01": 47,
  "2021-06-15": 15,
  "2021-03-19": 189,
  "2021-07-07": 31,
  "2021-06-16": 10,
  "2021-06-05": 49,
  "2021-06-18": 20,
  "2021-04-25": 24,
  "2021-07-02": 50,
  "2021-06-19": 135,
  "2020-09-02": 3,
  "2020-09-01": 2,
  "2020-09-05": 1,
  "2020-09-04": 11,
  "2021-06-03": 36,
  "2021-07-30": 505,
  "2021-04-23": 48,
  "2020-08-19": 93,
  "2021-05-15": 38,
  "2021-06-02": 50,
  "2021-05-14": 575,
  "2020-12-29": 457,
  "2021-04-22": 61,
  "2021-05-17": 14,
  "2021-05-16": 4,
  "2021-05-04": 79,
  "2021-04-30": 288,
  "2021-06-01": 49,
  "2021-07-08": 46,
  "2021-05-13": 156,
  "2021-04-21": 75,
  "2021-07-05": 19,
  "2021-07-06": 23,
  "2021-05-12": 23,
  "2021-07-01": 64,
  "2020-08-21": 29,
  "2021-07-03": 44,
  "2021-06-29": 4,
  "2021-05-25": 83
}
```

</details>
<br />

### List Trystero Samples

You can receive further details about each sample from any given daily corpus. Information included is similar to the output of `dfi list` with the addition of `bypasses` that denotes which provider was bypassed and `available_on_labs` which states the sample can be seen on [labs.inquest.net](https://labs.inquest.net/).


<details>
<summary>View example</summary>

```bash
$ inquestlabs trystero list-samples 2021-06-29 | jq .
[
  {
    "analysis_completed": true,
    "bypasses": "google,microsoft",
    "subcategory": "macro_hunter",
    "classification": "MALICIOUS",
    "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule",
    "file_type": "OLE",
    "image": false,
    "vt_positives": 3,
    "inquest_alerts": [
      {
        "category": "info",
        "description": "Detected macro logic that can write data to the file system.",
        "reference": null,
        "title": "Macro with File System Write"
      },
      {
        "category": "evasive",
        "description": "Detected a macro with an elusive start-up hook. These esoteric hooks result in automated macro logic execution which may not be detected by dynamic analysis systems.",
        "reference": null,
        "title": "Macro with Esoteric Startup Hook"
      },
      {
        "category": "info",
        "description": "Detected macro logic that will automatically execute on document open. Most malware contains some execution hook.",
        "reference": null,
        "title": "Macro with Startup Hook"
      },
      {
        "category": "malicious",
        "description": "An InQuest machine-learning model classified this macro as potentially malicious.",
        "reference": null,
        "title": "InQuest Machine Learning"
      },
      {
        "category": "suspicious",
        "description": "Detected macro logic that will load additional functionality from Dynamically Linked Libraries (DLLs). While not explicitly malicious, this is a common tactic for accessing APIs that are not otherwised exposed via Visual Basic for Applications (VBA).",
        "reference": null,
        "title": "Macro with DLL Reference"
      }
    ],
    "downloadable": true,
    "available_on_labs": true,
    "vt_weight": 0,
    "last_inquest_featext": "2021-06-28T04:16:36",
    "first_seen": "2021-06-28T04:15:47",
    "sha256": "c1df09944fe4eb4f7f86bd3a342e4548e584290167623959bca58acef4e25a1d",
    "mime_type": "application/cdfv2",
    "size": 1305088
  },
  {
    "analysis_completed": true,
    "bypasses": "microsoft",
    "subcategory": "macro_hunter",
    "classification": "MALICIOUS",
    "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule",
    "file_type": "OLE",
    "image": false,
    "vt_positives": 12,
    "inquest_alerts": [
      {
        "category": "info",
        "description": "Detected macro logic that can write data to the file system.",
        "reference": null,
        "title": "Macro with File System Write"
      },
      {
        "category": "info",
        "description": "Detected macro logic that will automatically execute on document open. Most malware contains some execution hook.",
        "reference": null,
        "title": "Macro with Startup Hook"
      },
      {
        "category": "info",
        "description": "Detected a macro with a suspicious string. Suspicious strings include privileged function calls, obfuscations, odd registry keys, etc...",
        "reference": null,
        "title": "Macro Contains Suspicious String"
      },
      {
        "category": "suspicious",
        "description": "Detected a macro that leverages Windows Management Instrumentation (WMI) functionality.",
        "reference": null,
        "title": "WMI Functionality"
      }
    ],
    "downloadable": true,
    "available_on_labs": true,
    "vt_weight": 6.199999809265137,
    "last_inquest_featext": "2021-06-28T12:14:44",
    "first_seen": "2021-06-28T12:13:41",
    "sha256": "59876f4baebcc78f3fcc944b24efb475f5030f6bb10190f4c07a6af5fa5c1568",
    "mime_type": "application/cdfv2",
    "size": 22528
  },
  {
    "analysis_completed": false,
    "bypasses": "google,microsoft",
    "subcategory": "maldoc_hunter",
    "classification": "MALICIOUS",
    "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maldoc_hunter.rule",
    "file_type": "OTHER",
    "image": false,
    "vt_positives": 9,
    "inquest_alerts": [
      {
        "category": "info",
        "description": "Found a Windows Portable Executable (PE) binary. Depending on context, the presence of a binary is suspicious or malicious.",
        "reference": null,
        "title": "Windows PE Executable"
      },
      {
        "category": "suspicious",
        "description": "Detected an ANSI or UNICODE http:// or https:// base64 encoded URL prefix.",
        "reference": null,
        "title": "Base64 Encoded URL"
      }
    ],
    "downloadable": false,
    "available_on_labs": false,
    "vt_weight": 5.800000190734863,
    "last_inquest_featext": null,
    "first_seen": "2021-06-28T12:58:56",
    "sha256": "bd736e5b4dc9e802a4b9c4cab0d1e0df872ce3c42091142d50b7520dc02abaad",
    "mime_type": "application/x-msi",
    "size": 4687360
  },
  {
    "analysis_completed": false,
    "bypasses": "microsoft",
    "subcategory": "maljar_hunter",
    "classification": "MALICIOUS",
    "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maljar_hunter.rule",
    "file_type": "OTHER",
    "image": false,
    "vt_positives": 9,
    "inquest_alerts": [],
    "downloadable": false,
    "available_on_labs": false,
    "vt_weight": 3.5999999046325684,
    "last_inquest_featext": null,
    "first_seen": "2021-06-28T13:43:23",
    "sha256": "e4ae2b5eb9b8549a322354dff9e88a0a356646351f5087e2d6ef91a630ef6007",
    "mime_type": "application/x-java-applet",
    "size": 19799
  }
]
```

</details>
