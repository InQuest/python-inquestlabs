import pytest

def test_repdb_list(labs):
    repdb_list= labs.repdb_list()
    assert len(repdb_list) == 1337

def test_repdb_list_with_key(labs_with_key):
    repdb_list= labs_with_key.repdb_list()
    assert len(repdb_list) == 1337
