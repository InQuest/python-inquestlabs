import pytest
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from inquestlabs import inquestlabs_api
from inquestlabs import inquestlabs_exception

@pytest.fixture
def labs():
    labs = inquestlabs_api()
    return labs

def test_api_invalid_method(labs):
    with pytest.raises(Exception)as excinfo:
        labs.API("mock", data=None, path=None, method="INVALID", raw=False)
    
    assert "AssertionError" in str(excinfo.type)

def test_api_invalid_path(labs):
    with pytest.raises(Exception) as excinfo:
        labs.API("mock", data=None, path="invalid", method="GET", raw=False)
    
    assert "FileNotFound" in str(excinfo.type)

def test_api_exceeded_attempts_to_communicate(labs,mocker):
        mocker.patch('requests.request' , side_effect=Exception)
        with pytest.raises(inquestlabs_exception) as excinfo:
            labs.API("mock")
        
        assert "attempts to communicate with InQuest" in str(excinfo.value)

# def test_api_bad_status_code(labs,mocker):
#     mocker.patch('inquestlabs.inquestlabs_api.API.response.status_code', return_value=400)
#     with pytest.raises(inquestlabs_exception) as excinfo:
#         labs.API("mock")
        
#     assert "status=400" in str(excinfo.value)

