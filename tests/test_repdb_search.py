import pytest


@pytest.fixture
def mock_list():
    return [{'created_date': 'Thu, 07 Nov 2019 00:09:16 GMT', 'data': 'opora-company.ru/O5Go/', 'data_type': 'url', 'derived': 'opora-company.ru', 'derived_type': 'domain', 'source': 'urlhaus', 'source_url': 'https://urlhaus.abuse.ch/host/opora-company.ru'}, {'created_date': 'Thu, 07 Nov 2019 00:09:04 GMT', 'data': '2toporaru.432.com1.ru/2.msi', 'data_type': 'url', 'derived': '2toporaru.432.com1.ru', 'derived_type': 'domain', 'source': 'urlhaus', 'source_url': 'https://urlhaus.abuse.ch/host/2toporaru.432.com1.ru'}, {'created_date': 'Thu, 07 Nov 2019 00:09:04 GMT', 'data': '2toporaru.432.com1.ru/1.msi', 'data_type': 'url', 'derived': '2toporaru.432.com1.ru', 'derived_type': 'domain', 'source': 'urlhaus', 'source_url': 'https://urlhaus.abuse.ch/host/2toporaru.432.com1.ru'}, {'created_date': 'Thu, 07 Nov 2019 00:09:02 GMT', 'data': '2toporaru.432.com1.ru/softcry.msi', 'data_type': 'url', 'derived': '2toporaru.432.com1.ru', 'derived_type': 'domain', 'source': 'urlhaus', 'source_url': 'https://urlhaus.abuse.ch/host/2toporaru.432.com1.ru'}, {'created_date': 'Sun, 27 Oct 2019 22:33:04 GMT', 'data': 'newnationaltradingcoporation.000webhostapp.com', 'data_type': 'url', 'derived': 'newnationaltradingcoporation.000webhostapp.com', 'derived_type': 'domain', 'source': 'threatweb', 'source_url': 'https://www.threatweb.com'}, {'created_date': 'Sun, 23 Jun 2019 13:55:46 GMT', 'data': 'www.dxaudio.com/styled-2/services/coporate.html', 'data_type': 'url', 'derived': 'www.dxaudio.com', 'derived_type': 'domain', 'source': 'threatweb', 'source_url': 'https://www.threatweb.com'}]


def test_repdb_search(labs, mock_list, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_list)
    repdb_list = labs.repdb_search("opora")
    assert len(repdb_list) == 6


def test_repdb_search_with_key(labs_with_key, mock_list, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_list)
    repdb_list = labs_with_key.repdb_search("opora")
    assert len(repdb_list) == 6
