import pytest

from inquestlabs import inquestlabs_exception
from unittest import mock

@pytest.fixture
def mock_invalid_doc():
    return r"test"

@pytest.fixture
def mock_valid_doc():
    return r"[\xD0\xCF]"

@pytest.fixture
def mock_valid_response():
    return {"success":True}

def test_invalid_upload_type(labs,mocker,mock_invalid_doc):
    mocker.patch("os.path.exists",return_value=True)
    mocker.patch("os.path.isfile",return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='invalid'),create=True)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_upload("mock")

    assert "unsupported file type" in str(excinfo.value)  

def test_valid_upload_type(labs,mocker,mock_valid_doc,mock_valid_response):
    mocker.patch("os.path.exists",return_value=True)
    mocker.patch("os.path.isfile",return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='PK'),create=True)
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_valid_response)
    response = labs.dfi_upload("mock")

    assert response["success"]  == True


def test_nonexistant_path(labs,mocker):
    mocker.patch("os.path.exists",return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_upload("mock")

    assert "invalid file" in str(excinfo.value)    

def test_path_is_not_a_file(labs,mocker):
    mocker.patch("os.path.isfile",return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_upload("mock")
        
    assert "invalid file" in str(excinfo.value)  

def test_invalid_upload_type_with_key(labs_with_key,mocker,mock_invalid_doc):
    mocker.patch("os.path.exists",return_value=True)
    mocker.patch("os.path.isfile",return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='invalid'),create=True)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_upload("mock")

    assert "unsupported file type" in str(excinfo.value)  

def test_valid_upload_type_with_key(labs_with_key,mocker,mock_valid_doc,mock_valid_response):
    mocker.patch("os.path.exists",return_value=True)
    mocker.patch("os.path.isfile",return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='PK'),create=True)
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_valid_response)
    response = labs_with_key.dfi_upload("mock")

    assert response["success"]  == True


def test_nonexistant_path_with_key(labs_with_key,mocker):
    mocker.patch("os.path.exists",return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_upload("mock")
        
    assert "invalid file" in str(excinfo.value)    

def test_path_is_not_a_file_with_key(labs_with_key,mocker):
    mocker.patch("os.path.isfile",return_value=False)
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_upload("mock")
        
    assert "invalid file" in str(excinfo.value)  

