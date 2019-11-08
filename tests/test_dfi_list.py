import pytest


def test_dfi_list(labs):
    dfi_list = labs.dfi_list()
    assert len(dfi_list) == 1337


def test_dfi_list_with_key(labs_with_key):
    dfi_list = labs_with_key.dfi_list()
    assert len(dfi_list) == 1337
