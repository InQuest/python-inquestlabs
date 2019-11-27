import pytest

@pytest.fixture()
def mock_repdb_list():
    return [ {'created_date': 'Sat, 16 Nov 2019 14:52:36 GMT',
  'data': 'techablog.com/PayPal-US/LLC/',
  'data_type': 'url',
  'derived': 'techablog.com',
  'derived_type': 'domain',
  'source': 'urlhaus',
  'source_url': 'https://urlhaus.abuse.ch/host/techablog.com'},
 {'created_date': 'Sat, 16 Nov 2019 14:52:36 GMT',
  'data': 'techquotes.tk/WIRE-FORM/IMT-368022645396/',
  'data_type': 'url',
  'derived': 'techquotes.tk',
  'derived_type': 'domain',
  'source': 'urlhaus',
  'source_url': 'https://urlhaus.abuse.ch/host/techquotes.tk'},
 {'created_date': 'Sat, 16 Nov 2019 14:52:36 GMT',
  'data': 'teplhome.ru/INV/WPD-4262802989/',
  'data_type': 'url',
  'derived': 'teplhome.ru',
  'derived_type': 'domain',
  'source': 'urlhaus',
  'source_url': 'https://urlhaus.abuse.ch/host/teplhome.ru'},
 {'created_date': 'Sat, 16 Nov 2019 14:52:36 GMT',
  'data': 'testypolicja.pl//WIRE-FORM/YQW-3280068/',
  'data_type': 'url',
  'derived': 'testypolicja.pl',
  'derived_type': 'domain',
  'source': 'urlhaus',
  'source_url': 'https://urlhaus.abuse.ch/host/testypolicja.pl'}]

def test_repdb_list(labs, mock_repdb_list,mocker):

    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_repdb_list)
    repdb_list = labs.repdb_list()
    assert len(repdb_list) == len(mock_repdb_list)


def test_repdb_list_with_key(labs_with_key, mock_repdb_list,mocker):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_repdb_list)
    repdb_list = labs_with_key.repdb_list()
    assert len(repdb_list) == len(mock_repdb_list)
