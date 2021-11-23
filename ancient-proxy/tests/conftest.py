import pytest

from brownie import Contract
from brownie import Dispatcher, BusinessLogicV1


@pytest.fixture(scope="module")
def bl_v1(accounts):
    owner = accounts[0]
    blv1 = BusinessLogicV1.deploy({"from": owner})
    disp = Dispatcher.deploy(blv1.address, {"from": owner})

    # blv1 runs on disp address
    return Contract.from_abi("BusinessLogicV1", disp.address, blv1.abi)
