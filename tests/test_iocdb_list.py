import pytest

@pytest.fixture
def mock_iocdb_list():
     return [ {'artifact': '149.202.154.164',
  'artifact_type': 'ipaddress',
  'created_date': 'Tue, 12 Nov 2019 08:59:41 GMT',
  'reference_link': 'https://twitter.com/SoulRage6/status/1194165760140201985',
  'reference_text': '#Nikki stealer C2 (probably) at: '
                    '149.202.154.]164/p/login.php\n'
                    'Also #Azorult panel on same IP: '
                    'http://149.202.154.]164/azo/index.php'},
 {'artifact': 'http://149.202.154.164/azo/index.php',
  'artifact_type': 'url',
  'created_date': 'Tue, 12 Nov 2019 08:59:41 GMT',
  'reference_link': 'https://twitter.com/SoulRage6/status/1194165760140201985',
  'reference_text': '#Nikki stealer C2 (probably) at: '
                    '149.202.154.]164/p/login.php\n'
                    'Also #Azorult panel on same IP: '
                    'http://149.202.154.]164/azo/index.php'},
 {'artifact': '217.114.181.3',
  'artifact_type': 'ipaddress',
  'created_date': 'Tue, 12 Nov 2019 08:59:41 GMT',
  'reference_link': 'https://twitter.com/sdpcthreatintel/status/1194163105376305153',
  'reference_text': '217.114.181.3 attempted MYSQL exploitation 1 time(s), '
                    'DShield attacks: 5, Country: RU'}]


def test_iocdb_list(labs,mocker, mock_iocdb_list):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_iocdb_list)
    iocdb_list = labs.iocdb_list()
    assert len(iocdb_list) == len(mock_iocdb_list)


def test_iocdb_list_with_key(labs_with_key, mocker, mock_iocdb_list):
    mocker.patch("inquestlabs.inquestlabs_api.API", return_value=mock_iocdb_list)
    iocdb_list = labs_with_key.iocdb_list()
    assert len(iocdb_list) == len(mock_iocdb_list)
