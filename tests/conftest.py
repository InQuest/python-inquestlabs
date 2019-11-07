import pytest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from inquestlabs import inquestlabs_api

@pytest.fixture(scope="module")
def labs():
    labs = inquestlabs_api()
    return labs

@pytest.fixture(scope="module")
def labs_with_key():
    labs_api = inquestlabs_api(api_key="mock")
    return labs_api