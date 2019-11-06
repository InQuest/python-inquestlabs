import pytest
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from inquestlabs import inquestlabs_api
from inquestlabs import inquestlabs_exception


@pytest.fixture
def labs():
    labs = inquestlabs_api()
    return labs

@pytest.fixture
def labs_with_key():
    labs_api = inquestlabs_api(api_key="mock")
    return labs_api

def test_dfi_filter_invalid(labs):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_attributes("mock",filter_by="invalid")
    
    assert "invalid attribute filter" in str(excinfo.value)



def test_dfi_filter_by_none(labs,mocker):
    mocker.patch("inquestlabs_api.__API")
    mock_attribs:[
           {
             "category": "ioc",
             "attribute": "domain",
             "count": 1,
             "value": "ancel.To"
           },
           {
             "category": "ioc",
             "attribute": "domain",
             "count": 1,
             "value": "Application.Top"
           }
         ]
    attributes = labs.dfi_attributes("mock")
    print(attributes)
