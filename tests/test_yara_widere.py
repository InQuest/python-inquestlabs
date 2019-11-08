import pytest
from inquestlabs import inquestlabs_exception


@pytest.fixture
def mock_body():
    return """(([\x2b\x2f-9A-Za-z][AQgw]BwAGUAZAByAGEAbQBhAG0AaQBuAG[k-n]|AHA{2}ZQBkAHIAYQBt(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[AQgw][A-D][\x2b\x2f-9A-Za-z]AGEAbQBpAG4Aa[Q-Za-f]|AHA{2}ZQBkAHIAYQBtA[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|[\x2b\x2f-9A-Za-z][AQgw]BwAGUAZAByAGEAb(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*A[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|[\x2b\x2f-9A-Za-z]{2}[048AEIMQUYcgkosw]AcABlAGQAcgBhAG(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z][AQgw]BhAG0AaQBuAG[k-n]|[\x2b\x2f-9A-Za-z][AQgw]BwAGUAZAByAGEAb(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[\x2b\x2f-9A-Za-z]A[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|AHA{2}ZQBkAHIAYQBt(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z][AQgw]BhAG0AaQBuAG[k-n]|[\x2b\x2f-9A-Za-z][AQgw]BwAGUAZAByAGEAb(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z][AQgw]BhAG0AaQBuAG[k-n]|[\x2b\x2f-9A-Za-z]{2}[048AEIMQUYcgkosw]AcABlAGQAcgBhAG0A[\x2b\x2f-9A-Za-z][AQgw]BhAG0AaQBuAG[k-n]|[\x2b\x2f-9A-Za-z][AQgw]BwAGUAZAByAGEAb(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[AQgw][A-D][\x2b\x2f-9A-Za-z]AGEAbQBpAG4Aa[Q-Za-f]|[\x2b\x2f-9A-Za-z]{2}[048AEIMQUYcgkosw]AcABlAGQAcgBhAG(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[\x2b\x2f-9A-Za-z]A[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|[\x2b\x2f-9A-Za-z]{2}[048AEIMQUYcgkosw]AcABlAGQAcgBhAG(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*A[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|AHA{2}ZQBkAHIAYQBt(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[\x2b\x2f-9A-Za-z]A[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|[\x2b\x2f-9A-Za-z]{2}[048AEIMQUYcgkosw]AcABlAGQAcgBhAG0AYQBtAGkAbgBp|AHA{2}ZQBkAHIAYQBtAGEAbQBpAG4Aa[Q-Za-f]|[\x2b\x2f-9A-Za-z]{2}[048AEIMQUYcgkosw]AcABlAGQAcgBhAG(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*[AQgw][A-D][\x2b\x2f-9A-Za-z]AGEAbQBpAG4Aa[Q-Za-f]|AHA{2}ZQBkAHIAYQBt(A[A-P]|[048AEIMQUYcgkosw]A[\x2b\x2f-9A-Za-z]|[AQgw][A-D]|[\x2b\x2f-9A-Za-z]A[A-P])*A[A-P][048AEIMQUYcgkosw]AYQBtAGkAbgBp|[\x2b\x2f-9A-Za-z][AQgw]BwAGUAZAByAGEAbQ[A-D][\x2b\x2f-9A-Za-z]AGEAbQBpAG4Aa[Q-Za-f])"""


@pytest.fixture
def mock_regex():
    return "pedram.*amini"


def test_valid_widere(labs, mocker, mock_body, mock_regex):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs.yara_widere(mock_regex)
    assert mock_body in results


def test_valid_widere_big_endian(labs, mock_regex, mocker, mock_body):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs.yara_widere(mock_regex, endian="BIG")
    assert mock_body in results


def test_valid_widere_little_endian(labs, mocker, mock_body, mock_regex):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs.yara_widere(mock_regex, endian="LITTLE")
    assert mock_body in results


def test_valid_widere_big_endian_with_key(labs_with_key, mock_regex, mocker, mock_body):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs_with_key.yara_widere(mock_regex, endian="BIG")
    assert mock_body in results


def test_valid_widere_little_endian_with_key(labs_with_key, mock_regex, mocker, mock_body):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs_with_key.yara_widere(mock_regex, endian="LITTLE")
    assert mock_body in results


def test_valid_widere_with_key(labs_with_key, mocker, mock_body, mock_regex):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_body)
    results = labs_with_key.yara_widere(mock_regex)
    assert mock_body in results


def test_invalid_endian(labs, mocker, mock_regex):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.yara_widere(mock_regex, endian="BAD_ENDIAN")

    assert "invalid endianess" in str(excinfo.value)


def test_invalid_endian_with_key(labs_with_key, mocker, mock_regex):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.yara_widere(mock_regex, endian="BAD_ENDIAN")

    assert "invalid endianess" in str(excinfo.value)
