import pytest
from brownie import EternalStorage, SocialLib, SocialSite


@pytest.fixture(scope="module")
def social_site_contract(accounts):
    owner = accounts[0]
    owner = accounts[0]
    es = EternalStorage.deploy({'from': owner})
    SocialLib.deploy({'from': owner})
    ss = SocialSite.deploy(es.address, {'from': owner})
    return ss