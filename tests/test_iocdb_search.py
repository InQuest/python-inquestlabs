import pytest


@pytest.fixture
def mock_list():
    return [{'artifact': 'worldwardmobi.com', 'artifact_type': 'domain', 'created_date': 'Thu, 07 Nov 2019 00:29:05 GMT', 'reference_link': 'https://twitter.com/IpNigh/status/1192232066064244736', 'reference_text': '#Phishing | #PhishKit | #PhishingKit Found and downloaded.\nURL:hxxps://worldwardmobi.com/icon/USAA/USAA/USAA\nThreat… https://twitter.com/i/w...'}, {'artifact': 'http://worldwardmobi.com/icon/USAA/USAA/USAA', 'artifact_type': 'url', 'created_date': 'Thu, 07 Nov 2019 00:29:05 GMT', 'reference_link': 'https://twitter.com/IpNigh/status/1192232066064244736', 'reference_text': '#Phishing | #PhishKit | #PhishingKit Found and downloaded.\nURL:hxxps://worldwardmobi.com/icon/USAA/USAA/USAA\nThreat… https://twitter.com/i/w...'}]


def test_iocdb_search(labs, mock_list, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_list)
    iocdb_list = labs.iocdb_search("worldwardmobi.com")
    assert len(iocdb_list) == 2


def test_iocdb_search_with_key(labs_with_key, mock_list, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_list)
    iocdb_list = labs_with_key.iocdb_search("worldwardmobi.com")
    assert len(iocdb_list) == 2
