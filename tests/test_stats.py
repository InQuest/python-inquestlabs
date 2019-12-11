import pytest


@pytest.fixture
def mock_stats():
    return {'dfidb': {'first_record': '2017-11-15', 'macro_hunter': 492225, 'maldoc_hunter': 117095, 'phish_hunter': 962, 'rtf_hunter': 8347, 'swfdoc_hunter': 1249}, 'dfiiocs': {'domain': 5074406, 'email': 1634109, 'filename': 8721261, 'first_record': '2017-11-15', 'ip': 1856861, 'url': 4077783, 'xmpid': 985797}, 'iocdb': {'domain': 24426, 'first_record': '2019-03-22', 'hash': 22370, 'ipaddress': 21457, 'url': 38528, 'yarasignature': 8508}, 'mime': {'application/cdfv2': 131773, 'application/msword': 151869, 'application/octet-stream': 3872, 'application/vnd.ms-excel': 160930, 'application/vnd.ms-office': 5907, 'application/vnd.ms-outlook': 9017, 'application/vnd.openxmlformats-officedocument.presentationml.presentation': 5144, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 99013, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 40795, 'application/zip': 5032, 'first_record': '2017-11-15'}, 'mime_high': {'DOC': 198571, 'DOCX': 5032, 'EML': 9017, 'OLE': 131773, 'OTHER': 3872, 'PPT': 5144, 'XLS': 259943, 'first_record': '2017-11-15'}, 'repdb': {'asn_num': 490, 'domain': 395391, 'first_record': '2018-04-01', 'ip': 5286304, 'url': 1299516}, 'repdbsources': {'abuse.ch': 556, 'alienvault': 1084460, 'bambenek': 12198, 'binarydefence': 123845, 'blocklist': 1913435, 'botscout': 69602, 'bruteforceblocker': 19056, 'ciarmy': 887942, 'cleantalk': 93800, 'csirtg': 86620, 'cybercrime-tracker': 2177, 'dataplane': 450594, 'emd': 255406, 'fedotracker': 3930, 'first_record': '2017-07-18', 'greensnow': 210190, 'isc.sans': 20903, 'malcode': 1051, 'malwaredomainlist': 3263, 'myip': 110129, 'openphish': 439857, 'packetmail': 447, 'phishtank': 165546, 'spamhaus': 490, 'sslbl': 604, 'stopforumspam': 15608, 'talos': 23227, 'threatweb': 745488, 'urlhaus': 235026, 'vxvault': 6053, 'zeus': 198}}


def test_stats(labs, mock_stats, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_stats)

    stats = labs.stats()
    assert "dfidb" in stats.keys()


def test_stats_with_key(labs_with_key, mock_stats, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=mock_stats)
    stats = labs_with_key.stats()
    assert "dfidb" in stats.keys()
