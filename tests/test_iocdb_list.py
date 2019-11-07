import pytest



def test_iocdb_list(labs):
    iocdb_list= labs.iocdb_list()
    assert len(iocdb_list) == 1337

def test_iocdb_list_with_key(labs_with_key):
    iocdb_list= labs_with_key.iocdb_list()
    assert len(iocdb_list) == 1337
