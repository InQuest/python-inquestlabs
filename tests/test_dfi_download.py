import pytest

from inquestlabs import inquestlabs_exception
import requests_mock
import requests

@pytest.fixture
def mock_invalid_doc():
    return "test"

@pytest.fixture
def mock_hash():
    return "06131f06c15c84d1e89a0401f0ce4eecf3508bef9492d7f2b2907f430be64e74'"

@pytest.fixture
def mock_hash_data():
    return bytearray('mock data inside this hash','utf-8')

def mock_invalid_hash_response(*args, **kwargs):
    with requests_mock.Mocker() as mock_request:
        mock_request.get("http://labs_mock.com", json={'error': "Supplied 'sha256' value is not a valid hash.", 'success': False}, status_code=400)
        response = requests.get("http://labs_mock.com")
        return response

def test_download_invalid_sha256(labs,mocker):
    mocker.patch('requests.request', side_effect=mock_invalid_hash_response)

    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_download("mock","fake_path")

    assert "value is not a valid hash" in str(excinfo.value)

def test_download_invalid_path(labs, mocker, mock_hash, mock_hash_data):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_hash_data)

    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_download(mock_hash,"/path/does/not/exist")

    assert "failed downloading file" in str(excinfo.value)


def test_download_invalid_sha256(labs_with_key,mocker):
    mocker.patch('requests.request', side_effect=mock_invalid_hash_response)

    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_download("mock","fake_path")

    assert "value is not a valid hash" in str(excinfo.value)

def test_download_invalid_path_with_key(labs_with_key, mocker, mock_hash, mock_hash_data):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_hash_data)

    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_download(mock_hash,"/path/does/not/exist")

    assert "failed downloading file" in str(excinfo.value)
