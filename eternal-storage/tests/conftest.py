import pytest
from brownie import EternalStorage, SocialLib, SocialSite, SocialLibV2, SocialSiteV2


@pytest.fixture(scope="module")
def social_site_contract(accounts):
    owner = accounts[0]
    es = EternalStorage.deploy({'from': owner})
    SocialLib.deploy({'from': owner})
    ss = SocialSite.deploy(es.address, {'from': owner})
    return ss

@pytest.fixture(scope="module")
def social_site_contract_v2(accounts):
    owner = accounts[0]
    es = EternalStorage.deploy({'from': owner})

    SocialLib.deploy({'from': owner})
    ssv1 = SocialSite.deploy(es.address, {'from': owner})

    SocialLibV2.deploy({'from': owner})
    ssv2 = SocialSiteV2.deploy(es.address, {'from': owner})
    return ssv1, ssv2

