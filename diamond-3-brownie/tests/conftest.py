import pytest
from brownie import Contract
from scripts.helpers import facetCutAction, getSelectors


@pytest.fixture(scope="module")
def deployed_contracts(
    accounts,
    Diamond,
    DiamondInit,
    DiamondCutFacet,
    DiamondLoupeFacet,
    OwnershipFacet,
    Test1Facet,
    Test2Facet,
):
    owner = accounts[0]

    diamondCutFacet = DiamondCutFacet.deploy({"from": owner})
    diamondLoupeFacet = DiamondLoupeFacet.deploy({"from": owner})
    ownershipFacet = OwnershipFacet.deploy({"from": owner})
    test1Facet = Test1Facet.deploy({"from": owner})
    test2Facet = Test2Facet.deploy({"from": owner})

    diamondInit = DiamondInit.deploy({"from": owner})
    diamond = Diamond.deploy(owner, diamondCutFacet.address, {"from": owner})

    cut = [
        [
            diamondLoupeFacet.address,
            facetCutAction["Add"],
            getSelectors(DiamondLoupeFacet),
        ],
        [ownershipFacet.address, facetCutAction["Add"], getSelectors(OwnershipFacet)],
    ]

    # DiamondCutFacet at diamond.address
    diamondCut = Contract.from_abi("DiamondCut", diamond.address, diamondCutFacet.abi)

    # DiamondInit has only one function, init()
    initSelector = getSelectors(DiamondInit)[0]

    # Cutting the Diamond
    diamondCut.diamondCut(cut, diamondInit.address, initSelector, {"from": owner})

    return (
        diamond,
        diamondCutFacet,
        diamondLoupeFacet,
        ownershipFacet,
        test1Facet,
        test2Facet,
    )
