import pytest


@pytest.fixture
def mock_uint_response():
    return "/* trigger = 'deadbeef' */\n(uint32be(0x0) == 0x64656164 and uint32be(0x4) == 0x62656566)"


@pytest.fixture
def mock_input():
    return "deadbeef"


def test_uint_valid(labs, mock_uint_response, mock_input, mocker):
    mocker.patch("inquestlabs.inquestlabs_api.API",
                 return_value=mock_uint_response)
    response = labs.yara_uint(mock_input)
    assert mock_uint_response in response


def test_uint_valid_with_key(labs_with_key, mock_uint_response, mock_input, mocker):
    mocker.patch("inquestlabs.inquestlabs_api.API",
                 return_value=mock_uint_response)
    response = labs_with_key.yara_uint(mock_input)
    assert mock_uint_response in response
