import pytest
from brownie import Contract
from scripts.helpers import (
    hashFunctionSignature,
    getSelectors,
    zeroAddress,
    facetCutAction,
)


def test_add_test1_and_test2_facet_functions(accounts, deployed_contracts):
    owner = accounts[0]

    diamond = deployed_contracts[0]
    diamondCutFacet = deployed_contracts[1]
    diamondLoupeFacet = deployed_contracts[2]
    test1Facet = deployed_contracts[4]
    test2Facet = deployed_contracts[5]

    test1FacetSelectors = getSelectors(test1Facet)
    test1FacetSelectors.remove(hashFunctionSignature("supportsInterface(bytes4)"))

    cut = [
        [test1Facet.address, facetCutAction["Add"], test1FacetSelectors],
        [test2Facet.address, facetCutAction["Add"], getSelectors(test2Facet)],
    ]

    diamondCut = Contract.from_abi("DiamondCut", diamond.address, diamondCutFacet.abi)

    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )

    diamondLoupe = Contract.from_abi(
        "DiamondLoupe", diamond.address, diamondLoupeFacet.abi
    )

    facets = diamondLoupe.facets()

    assert len(facets) == 5
