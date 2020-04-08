# python-inquestlabs
A Pythonic interface and command line tool for interacting with the InQuest Labs API.

## InQuest Labs Command Line Driver
```
Usage:
    inquestlabs [options] dfi list
    inquestlabs [options] dfi details <sha256> [--attributes]
    inquestlabs [options] dfi download <sha256> <path>
    inquestlabs [options] dfi attributes <sha256> [--filter=<filter>]
    inquestlabs [options] dfi search (code|context|metadata|ocr) <keyword>
    inquestlabs [options] dfi search (md5|sha1|sha256|sha512) <hash>
    inquestlabs [options] dfi search (domain|email|filename|ip|url|xmpid) <ioc>
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
    inquestlabs [options] stats

Options:
    --api=<apikey>      Specify an API key.
    --config=<config>   Configuration file with API key [default: ~/.iqlabskey].
    --debug             Docopt debugging.
    --filter=<filter>   Filter by attributes type (domain, email, filename, ip, url, xmpid)
    -h --help           Show this screen.
    --hex               Treat <instring> as hex bytes.
    -l --limits         Show remaining API credits and limit reset window.
    --proxy=<proxy>     Intermediate proxy
    --verbose=<level>   Verbosity level, outputs to stderr [default: 0].
    --version           Show version.
```

## Testing

Use pytest to test each case (or individually by specifying which file to test):

`pytest tests/*`
