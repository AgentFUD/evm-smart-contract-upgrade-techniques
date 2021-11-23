from scripts.helpers import getSelectors, facetCutAction


def test_contracts_deployed(contracts):
    for contract in contracts:
        assert len(contract.address) == 42


def test_diamond_has_three_facets(contracts):
    diamondLoupe = contracts[2]
    assert len(diamondLoupe.facetAddresses()) == 3


def test_facets_have_the_right_function_selectors(contracts):
    diamondCut = contracts[1]
    diamondLoupe = contracts[2]
    ownership = contracts[3]

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


def test_selectors_associated_to_facets_correctly(contracts):
    diamondLoupe = contracts[2]
    facetAddresses = diamondLoupe.facetAddresses()
    assert diamondLoupe.facetAddress("0x1f931c1c") == facetAddresses[0]
    assert diamondLoupe.facetAddress("0xcdffacc6") == facetAddresses[1]
    assert diamondLoupe.facetAddress("0x01ffc9a7") == facetAddresses[1]
    assert diamondLoupe.facetAddress("0xf2fde38b") == facetAddresses[2]
