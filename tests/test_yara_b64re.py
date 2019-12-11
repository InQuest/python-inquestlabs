import pytest
from inquestlabs import inquestlabs_exception


@pytest.fixture
def mock_body():
    return """([\x2b\x2f-9A-Za-z][3HXn]BlZHJhb([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z][159BFJNRVZdhlptx]hbWlua[Q-Za-f]|[\x2b\x2f-9A-Za-z]{2}[159BFJNRVZdhlptx]wZWRyYW[0-3][\x2b\x2f-9A-Za-z]YW1pbm[k-n]|[\x2b\x2f-9A-Za-z][3HXn]BlZHJhb([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z]{2}[2GWm]FtaW5p|cGVkcmFt([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z][159BFJNRVZdhlptx]hbWlua[Q-Za-f]|[\x2b\x2f-9A-Za-z][3HXn]BlZHJhb([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z]{2}YW1pbm[k-n]|cGVkcmFtYW1pbm[k-n]|[\x2b\x2f-9A-Za-z]{2}[159BFJNRVZdhlptx]wZWRyYW1hbWlua[Q-Za-f]|cGVkcmFt([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z][2GWm]FtaW5p|[\x2b\x2f-9A-Za-z][3HXn]BlZHJhb([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z][2GWm]FtaW5p|[\x2b\x2f-9A-Za-z]{2}[159BFJNRVZdhlptx]wZWRyYW([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z]{2}[2GWm]FtaW5p|[\x2b\x2f-9A-Za-z][3HXn]BlZHJhbWFtaW5p|cGVkcmFt([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z]{2}[2GWm]FtaW5p|cGVkcmFt([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z]{2}YW1pbm[k-n]|cGVkcmFt[\x2b\x2f-9A-Za-z][2GWm]FtaW5p|[\x2b\x2f-9A-Za-z]{2}[159BFJNRVZdhlptx]wZWRyYW([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z]{2}YW1pbm[k-n]|[\x2b\x2f-9A-Za-z][3HXn]BlZHJhb[Q-Za-f][159BFJNRVZdhlptx]hbWlua[Q-Za-f]|[\x2b\x2f-9A-Za-z]{2}[159BFJNRVZdhlptx]wZWRyYW([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z][2GWm]FtaW5p|[\x2b\x2f-9A-Za-z]{2}[159BFJNRVZdhlptx]wZWRyYW([\x2b\x2f-9A-Za-z][\x2b\x2f-9A-Za-z]|[\x2b\x2f-9A-Za-z])*[\x2b\x2f-9A-Za-z][159BFJNRVZdhlptx]hbWlua[Q-Za-f])"""


@pytest.fixture
def mock_regex():
    return "pedram.*amini"


def test_valid_b64re(labs, mocker, mock_body, mock_regex):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs.yara_b64re(mock_regex)
    assert mock_body in results


def test_valid_b64re_big_endian(labs, mock_regex, mocker, mock_body):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs.yara_b64re(mock_regex, endian="BIG")
    assert mock_body in results


def test_valid_b64re_little_endian(labs, mocker, mock_body, mock_regex):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs.yara_b64re(mock_regex, endian="LITTLE")
    assert mock_body in results


def test_valid_b64re_big_endian_with_key(labs_with_key, mock_regex, mocker, mock_body):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs_with_key.yara_b64re(mock_regex, endian="BIG")
    assert mock_body in results


def test_valid_b64re_little_endian_with_key(labs_with_key, mock_regex, mocker, mock_body):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs_with_key.yara_b64re(mock_regex, endian="LITTLE")
    assert mock_body in results


def test_valid_b64re_with_key(labs_with_key, mocker, mock_body, mock_regex):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs_with_key.yara_b64re(mock_regex)
    assert mock_body in results


def test_invalid_endian(labs, mocker, mock_regex):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.yara_b64re(mock_regex, endian="BAD_ENDIAN")

    assert "invalid endianess" in str(excinfo.value)


def test_invalid_endian_with_key(labs_with_key, mocker, mock_regex):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.yara_b64re(mock_regex, endian="BAD_ENDIAN")

    assert "invalid endianess" in str(excinfo.value)
