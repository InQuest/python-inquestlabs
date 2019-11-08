import pytest


def test_iocdb_sources(labs):
    iocdb_list = labs.iocdb_sources()
    assert len(iocdb_list) > 0


def test_iocdb_sources_with_key(labs_with_key):
    iocdb_list = labs_with_key.iocdb_sources()
    assert len(iocdb_list) > 0
