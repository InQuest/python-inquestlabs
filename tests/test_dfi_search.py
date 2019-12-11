import pytest
from inquestlabs import inquestlabs_exception
import json

@pytest.fixture
def mock_response():
    response = """{
  "data": [
    {
      "analysis_completed": true,
      "classification": "UNKNOWN",
      "file_type": "XLS",
      "first_seen": "Wed, 16 Oct 2019 16:55:16 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Mon, 28 Oct 2019 06:39:05 GMT",
      "len_code": 8415,
      "len_context": 35268,
      "len_metadata": 11294,
      "len_ocr": 88,
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "sha256": "b43e1cef3c40e4629529c0ddcdef3c5be451477afd713abd0b67e1260831ba19",
      "size": 2004642,
      "subcategory": "macro_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule"
    },
    {
      "analysis_completed": true,
      "classification": "UNKNOWN",
      "file_type": "XLS",
      "first_seen": "Wed, 16 Oct 2019 16:55:13 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Sun, 27 Oct 2019 17:28:11 GMT",
      "len_code": 10154,
      "len_context": 20688,
      "len_metadata": 13595,
      "len_ocr": 88,
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "sha256": "0d85df8baeedddcf487865eb3bf827399895f1e470675a6542135848514f5003",
      "size": 2044782,
      "subcategory": "macro_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule"
    },
    {
      "analysis_completed": true,
      "classification": "UNKNOWN",
      "file_type": "XLS",
      "first_seen": "Wed, 16 Oct 2019 16:09:02 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Mon, 28 Oct 2019 08:37:09 GMT",
      "len_code": 10508,
      "len_context": 20674,
      "len_metadata": 13595,
      "len_ocr": 88,
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "sha256": "cadffb3d09a59d0923ddf57982096383cf44f9016007000a81fa56e875fceaa1",
      "size": 2069673,
      "subcategory": "macro_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule"
    }],"success": true}"""
    return json.loads(response)


def test_invalid_category(labs, mocker):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_search("BAD_CATEGORY", "code", "mock_keyword")

    assert "invalid category" in str(excinfo.value)


def test_invalid_subcategory(labs, mocker):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs.dfi_search("hash", "BAD_CATEGORY", "mock_keyword")
    assert "invalid subcategory" in str(excinfo.value)


def test_valid_ext(labs, mocker, mock_response):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    results = labs.dfi_search("ext", "metadata", "mock")
    assert len(results["data"]) == 3


def test_valid_hash(labs, mocker, mock_response):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    results = labs.dfi_search("hash", "md5", "mock")
    assert len(results["data"]) == 3


def test_valid_other(labs, mocker, mock_response):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    results = labs.dfi_search("ioc", "domain", "mock")
    assert len(results["data"]) == 3


def test_invalid_category_with_key(labs_with_key, mocker):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_search("BAD_CATEGORY", "code", "mock_keyword")

    assert "invalid category" in str(excinfo.value)


def test_invalid_subcategory_with_key(labs_with_key, mocker):
    with pytest.raises(inquestlabs_exception) as excinfo:
        labs_with_key.dfi_search("hash", "BAD_CATEGORY", "mock_keyword")

    assert "invalid subcategory" in str(excinfo.value)


def test_valid_ext_with_key(labs_with_key, mocker, mock_response):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    results = labs_with_key.dfi_search("ext", "metadata", "mock")
    assert len(results["data"]) == 3


def test_valid_hash_with_key(labs_with_key, mocker, mock_response):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    results = labs_with_key.dfi_search("hash", "md5", "mock")
    assert len(results["data"]) == 3


def test_valid_other_with_key(labs_with_key, mocker, mock_response):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_response)
    results = labs_with_key.dfi_search("ioc", "domain", "mock")
    assert len(results["data"]) == 3
