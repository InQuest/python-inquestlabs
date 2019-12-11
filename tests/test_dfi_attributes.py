import pytest
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from inquestlabs import inquestlabs_exception
from inquestlabs import inquestlabs_api

@pytest.fixture
def mock_attribs():
    return [
        {"attribute": "domain",
         "category": "ioc",
         "count": 1,
         "value": "aHX3xw.ao"
         },
        {"attribute": "domain",
         "category": "ioc",
         "count": 1,
         "value": "aHX3xw.bt"
         },
        {"attribute": "url",
         "category": "ioc",
         "count": 1,
         "value": "aHX3xw.bt"
         },
        {"attribute": "email",
         "category": "ioc",
         "count": 1,
         "value": "aHX3xw.bt"
         },
        {"attribute": "domain",
         "category": "ioc",
         "count": 1,
         "value": "ebug.Pr"
         },
        {"attribute": "domain",
         "category": "ioc",
         "count": 1,
            "value": "Paint.NET"
         },
        {"attribute": "filename",
         "category": "ioc",
         "count": 1,
         "value": "FM20.DLL"
         },
        {"attribute": "filename",
         "category": "ioc",
         "count": 1,
         "value": "MSO.DLL"
         },
        {"attribute": "filename",
         "category": "ioc",
         "count": 1,
         "value": "VBE7.DLL"
         },
        {"attribute": "xmpid",
         "category": "ioc",
         "count": 1,
         "value": "xmp.iid:c69177cd-9fe4-7044-be5a-e60c0cec53fb"},
        {"attribute": "xmpid",
         "category": "ioc",
         "count": 1,
         "value": "xmp.iid:dc986887-b6b9-324c-afbd-cf38bd4f373e"
         }]


@pytest.fixture
def mock_attribs():
    return [
        {"attribute": "domain",
         "category": "ioc", 
         "count": 1,
          "value": "aHX3xw.ao"
        },
        {"attribute": "domain",
         "category": "ioc",
          "count": 1,
           "value": "aHX3xw.bt"
        },
        {"attribute": "url",
         "category": "ioc",
          "count": 1,
           "value": "aHX3xw.bt"
        },
        {"attribute": "email",
         "category": "ioc",
          "count": 1,
           "value": "aHX3xw.bt"
        },
        {"attribute": "domain",
         "category": "ioc", 
         "count": 1, 
         "value": "ebug.Pr"
         },
         {"attribute": "domain",
          "category": "ioc",
           "count": 1,
            "value": "Paint.NET"
        }, 
        {"attribute": "filename",
         "category": "ioc", 
         "count": 1, 
         "value": "FM20.DLL"
        }, 
        {"attribute": "filename",
         "category": "ioc",
          "count": 1, 
          "value": "MSO.DLL"
        }, 
        {"attribute": "filename",
         "category": "ioc", 
         "count": 1, 
         "value": "VBE7.DLL"
        }, 
        {"attribute": "xmpid",
         "category": "ioc",
          "count": 1,
         "value": "xmp.iid:c69177cd-9fe4-7044-be5a-e60c0cec53fb"},
        {"attribute": "xmpid",
         "category": "ioc",
          "count": 1, 
          "value": "xmp.iid:dc986887-b6b9-324c-afbd-cf38bd4f373e"
        }]

@pytest.fixture
def mock_attribs():
    return [
        {"attribute": "domain",
         "category": "ioc", 
         "count": 1,
          "value": "aHX3xw.ao"
        },
        {"attribute": "domain",
         "category": "ioc",
          "count": 1,
           "value": "aHX3xw.bt"
        },
        {"attribute": "url",
         "category": "ioc",
          "count": 1,
           "value": "aHX3xw.bt"
        },
        {"attribute": "email",
         "category": "ioc",
          "count": 1,
           "value": "aHX3xw.bt"
        },
        {"attribute": "domain",
         "category": "ioc", 
         "count": 1, 
         "value": "ebug.Pr"
         },
         {"attribute": "domain",
          "category": "ioc",
           "count": 1,
            "value": "Paint.NET"
        }, 
        {"attribute": "filename",
         "category": "ioc", 
         "count": 1, 
         "value": "FM20.DLL"
        }, 
        {"attribute": "filename",
         "category": "ioc",
          "count": 1, 
          "value": "MSO.DLL"
        }, 
        {"attribute": "filename",
         "category": "ioc", 
         "count": 1, 
         "value": "VBE7.DLL"
        }, 
        {"attribute": "xmpid",
         "category": "ioc",
          "count": 1,
         "value": "xmp.iid:c69177cd-9fe4-7044-be5a-e60c0cec53fb"},
        {"attribute": "xmpid",
         "category": "ioc",
          "count": 1, 
          "value": "xmp.iid:dc986887-b6b9-324c-afbd-cf38bd4f373e"
        }]

def test_dfi_filter_invalid(labs):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_attributes("mock", filter_by="invalid")

    assert "invalid attribute filter" in str(excinfo.value)


def test_dfi_filter_by_domain(labs, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs.dfi_attributes("mock", filter_by="domain")
    assert len(attributes) == 4


def test_dfi_filter_by_xmpid(labs, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs.dfi_attributes("mock", filter_by="xmpid")
    assert len(attributes) == 2


def test_dfi_filter_by_url(labs, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs.dfi_attributes("mock", filter_by="url")
    assert len(attributes) == 1


def test_dfi_filter_by_email(labs, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs.dfi_attributes("mock", filter_by="email")
    assert len(attributes) == 1


def test_dfi_filter_by_filename(labs, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs.dfi_attributes("mock", filter_by="filename")
    assert len(attributes) == 3


def test_dfi_filter_by_none(labs, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)

    attributes = labs.dfi_attributes("mock")
    assert len(attributes) == 11


def test_dfi_filter_invalid_with_key(labs_with_key):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_attributes("mock", filter_by="invalid")

    assert "invalid attribute filter" in str(excinfo.value)


def test_dfi_filter_by_domain_with_key(labs_with_key, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs_with_key.dfi_attributes("mock", filter_by="domain")
    assert len(attributes) == 4


def test_dfi_filter_by_xmpid_with_key(labs_with_key, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs_with_key.dfi_attributes("mock", filter_by="xmpid")
    assert len(attributes) == 2


def test_dfi_filter_by_url_with_key(labs_with_key, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs_with_key.dfi_attributes("mock", filter_by="url")
    assert len(attributes) == 1


def test_dfi_filter_by_email_with_key(labs_with_key, mocker, mock_attribs):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs_with_key.dfi_attributes("mock", filter_by="email")
    assert len(attributes) == 1


def test_dfi_filter_by_filename_with_key(labs_with_key, mocker, mock_attribs):

    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs_with_key.dfi_attributes("mock", filter_by="filename")
    assert len(attributes) == 3


def test_dfi_filter_by_none_with_key(labs_with_key, mocker, mock_attribs):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_attribs)
    attributes = labs_with_key.dfi_attributes("mock")
    assert len(attributes) == 11
