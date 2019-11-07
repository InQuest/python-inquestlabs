import pytest


def test_dfi_sources(labs):
    dfi_list= labs.dfi_sources()
    assert len(dfi_list) >0

def test_dfi_sources_with_key(labs_with_key):
    dfi_list= labs_with_key.dfi_sources()
    assert len(dfi_list) > 0
