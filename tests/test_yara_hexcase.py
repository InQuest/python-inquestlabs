import pytest


@pytest.fixture
def mock_input():
    return "pedram"


@pytest.fixture
def mock_response():
    return "[57]0[46]5[46]4[57]2[46]1[46]d"


def test_valid_hexcase(labs, mock_input, mock_response, mocker):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    response = labs.yara_hexcase(mock_input)
    assert mock_response in response


def test_valid_hexcase_with_key(labs_with_key, mock_input, mock_response, mocker):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    response = labs_with_key.yara_hexcase(mock_input)
    assert mock_response in response
