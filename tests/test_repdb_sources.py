import pytest


def test_repdb_sources(labs,mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=["source1","source2","etc"])

    repdb_sources = labs.repdb_sources()
    assert len(repdb_sources) > 0


def test_repdb_sources_with_key(labs_with_key,mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API', return_value=["source1","source2","etc"])

    repdb_sources = labs_with_key.repdb_sources()
    assert len(repdb_sources) > 0
