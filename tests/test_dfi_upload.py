import pytest

from inquestlabs import inquestlabs_exception


@pytest.fixture
def mock_invalid_doc():
    return "test"


@pytest.fixture
def mock_valid_doc():
    return "[\xD0\xCF]"


@pytest.fixture
def mock_valid_response():
    return {"success": True}


def test_invalid_upload_type(labs, mocker, mock_invalid_doc):
    mock_file = mocker.mock_open(read_data=mock_invalid_doc)
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch('builtins.open', mock_file)
    mocker.patch('inquestlabs.inquestlabs_api.API',
                 return_value=mock_valid_response)
    with pytest.raises(inquestlabs_exception, match=r'unsupported file type for upload'):
        labs.dfi_upload("mock")


def test_valid_upload_type(labs, mocker, mock_valid_doc, mock_valid_response):
    mock_file = mocker.mock_open(read_data=b'PK')
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch('builtins.open', mock_file)
    mocker.patch('inquestlabs.inquestlabs_api.API',
                 return_value=mock_valid_response)
    response = labs.dfi_upload("mock")
    assert response["success"]


def test_nonexistant_path(labs, mocker):
    mocker.patch("os.path.exists", return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_upload("mock")

    assert "invalid file" in str(excinfo.value)


def test_path_is_not_a_file(labs, mocker):
    mocker.patch("os.path.isfile", return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_upload("mock")

    assert "invalid file" in str(excinfo.value)


def test_invalid_upload_type_with_key(labs_with_key, mocker, mock_invalid_doc):
    mock_file = mocker.mock_open(read_data=mock_invalid_doc)
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch('builtins.open', mock_file)
    mocker.patch('inquestlabs.inquestlabs_api.API',
                 return_value=mock_valid_response)
    with pytest.raises(inquestlabs_exception, match=r'unsupported file type for upload'):
        labs_with_key.dfi_upload("mock")


def test_valid_upload_type_with_key(labs_with_key, mocker, mock_valid_doc, mock_valid_response):
    mock_file = mocker.mock_open(read_data=b'PK')
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch('builtins.open', mock_file, create=True)
    mocker.patch('inquestlabs.inquestlabs_api.API',
                 return_value=mock_valid_response)
    response = labs_with_key.dfi_upload("mock")

    assert response["success"]


def test_nonexistant_path_with_key(labs_with_key, mocker):
    mocker.patch("os.path.exists", return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_upload("mock")
    assert "invalid file" in str(excinfo.value)


def test_path_is_not_a_file_with_key(labs_with_key, mocker):
    mocker.patch("os.path.isfile", return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_upload("mock")

    assert "invalid file" in str(excinfo.value)
