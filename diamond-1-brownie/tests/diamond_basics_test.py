from scripts.helpers import getSelectors
from brownie import Contract


def test_contracts_deployed(deployed_contracts):
    for contract in deployed_contracts:
        assert len(contract.address) == 42


def test_diamond_has_three_facets(deployed_contracts):
    diamond = deployed_contracts[0]
    diamondLoupeFacet = deployed_contracts[2]
    diamondLoupe = Contract.from_abi(
        "DiamondLoupe", diamond.address, diamondLoupeFacet.abi
    )
    assert len(diamondLoupe.facetAddresses()) == 3


def test_facets_have_the_right_function_selectors(deployed_contracts):
    diamond = deployed_contracts[0]
    diamondLoupeFacet = deployed_contracts[2]
    diamondCutFacet = deployed_contracts[1]
    ownership = deployed_contracts[3]

    diamondLoupe = Contract.from_abi(
        "DiamondLoupe", diamond.address, diamondLoupeFacet.abi
    )
    diamondCut = Contract.from_abi("DiamondCut", diamond.address, diamondCutFacet.abi)

    facetAddresses = diamondLoupe.facetAddresses()

    selectors = getSelectors(diamondCut)
    result = diamondLoupe.facetFunctionSelectors(facetAddresses[0])
    assert selectors == list(result)

    selectors = getSelectors(diamondLoupe)
    result = diamondLoupe.facetFunctionSelectors(facetAddresses[1])
    assert selectors == list(result)

    selectors = getSelectors(ownership)
    result = diamondLoupe.facetFunctionSelectors(facetAddresses[2])
    assert selectors == list(result)


def test_selectors_associated_to_facets_correctly(deployed_contracts):
    diamond = deployed_contracts[0]
    diamondLoupeFacet = deployed_contracts[2]
    diamondLoupe = Contract.from_abi(
        "DiamondLoupe", diamond.address, diamondLoupeFacet.abi
    )
    facetAddresses = diamondLoupe.facetAddresses()
    assert diamondLoupe.facetAddress("0x1f931c1c") == facetAddresses[0]
    assert diamondLoupe.facetAddress("0xcdffacc6") == facetAddresses[1]
    assert diamondLoupe.facetAddress("0x01ffc9a7") == facetAddresses[1]
    assert diamondLoupe.facetAddress("0xf2fde38b") == facetAddresses[2]
