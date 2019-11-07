import pytest

def test_repdb_sources(labs):
    repdb_sources= labs.repdb_sources()
    assert len(repdb_sources) > 0

def test_repdb_sources_with_key(labs_with_key):
    repdb_sources= labs_with_key.repdb_sources()
    assert len(repdb_sources) > 0
