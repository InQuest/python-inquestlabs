import pytest
import sys, os
import json
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from inquestlabs import inquestlabs_api
from inquestlabs import inquestlabs_exception

@pytest.fixture
def labs():
    labs = inquestlabs_api()
    return labs

@pytest.fixture
def labs_with_key():
    labs_api = inquestlabs_api(api_key="mock")
    return labs_api


def test_iocdb_sources(labs):
    iocdb_list= labs.iocdb_sources()
    assert len(iocdb_list) >0

def test_iocdb_sources_with_key(labs_with_key):
    iocdb_list= labs_with_key.iocdb_sources()
    assert len(iocdb_list) > 0
