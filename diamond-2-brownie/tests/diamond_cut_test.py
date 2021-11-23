import pytest
from scripts.helpers import (
    getSelectors,
    facetCutAction,
    zeroAddress,
    hashFunctionSignature,
)
from brownie import Contract


def test_add_test1facet_functions(accounts, contracts, Test1Facet):
    owner = accounts[0]
    diamondLoupe = contracts[2]
    diamondCut = contracts[1]
    test1Facet = contracts[4]

    # removing supportsInterface(bytes4) from selector list
    supportsInterFaceFnSignature = "supportsInterface(bytes4)"
    selector = hashFunctionSignature(supportsInterFaceFnSignature)
    selectors = getSelectors(Test1Facet)
    selectors.remove(selector)

    cut = [[test1Facet.address, facetCutAction["Add"], selectors]]
    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )

    assert len(diamondLoupe.facetAddresses()) == 4


def test_call_test1facet_functions(accounts, contracts, Test1Facet):
    owner = accounts[0]
    diamond = contracts[0]
    diamondLoupe = contracts[2]
    test1 = contracts[4]
    test1AtDiamond = Contract.from_abi("Test1Facet", diamond.address, Test1Facet.abi)

    test1AtDiamond.test1Func3({"from": owner})
    test1AtDiamond.test1Func19({"from": owner})

    assert len(diamondLoupe.facetFunctionSelectors(test1.address)) == 20


def test_replace_supportsInterface_function(accounts, contracts):
    owner = accounts[0]
    diamondCut = contracts[1]
    diamondLoupe = contracts[2]
    test1 = contracts[4]

    assert len(diamondLoupe.facetFunctionSelectors(test1.address)) == 20

    function_signature = str = "supportsInterface(bytes4)"
    selector = hashFunctionSignature(function_signature_text=function_signature)
    cut = [[test1.address, facetCutAction["Replace"], [selector]]]

    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )

    assert len(diamondLoupe.facetFunctionSelectors(test1.address)) == 21


def test_add_test2facet_functions(accounts, contracts, Test2Facet):
    owner = accounts[0]
    diamondCut = contracts[1]
    diamondLoupe = contracts[2]
    test2 = contracts[5]

    cut = [[test2.address, facetCutAction["Add"], getSelectors(Test2Facet)]]

    # Cut the Diamond
    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )

    selectors = getSelectors(test2)
    z = diamondLoupe.facetFunctionSelectors(test2.address)
    assert len(z) == 20
    assert selectors == list(z)


def test_test2facet_call(accounts, contracts, Test2Facet):
    owner = accounts[0]
    diamond = contracts[0]
    test2AtDiamond = Contract.from_abi("Test2Facet", diamond.address, Test2Facet.abi)
    test2AtDiamond.test2Func9({"from": owner})


def test_remove_some_test2facet_functions(accounts, contracts):
    owner = accounts[0]
    diamondCut = contracts[1]
    diamondLoupe = contracts[2]
    test2 = contracts[5]

    functions_to_remove = [
        "test2Func1()",
        "test2Func5()",
        "test2Func6()",
        "test2Func19()",
        "test2Func20()",
    ]
    selectors_to_remove = [
        hashFunctionSignature(fname) for fname in functions_to_remove
    ]

    cut = [[zeroAddress, facetCutAction["Remove"], selectors_to_remove]]

    # Cut the Diamond
    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )
    function_selectors = diamondLoupe.facetFunctionSelectors(test2.address)
    assert len(function_selectors) == 15
    for fsr in selectors_to_remove:
        if fsr in function_selectors:
            assert False


def test_remove_some_test1facet_functions(accounts, contracts):
    owner = accounts[0]
    diamondCut = contracts[1]
    diamondLoupe = contracts[2]
    test1 = contracts[4]

    functions_to_remove = [
        "test1Func1()",
        "test1Func5()",
        "test1Func6()",
        "test1Func11()",
        "test1Func19()",
        "test1Func20()",
    ]
    selectors_to_remove = [
        hashFunctionSignature(fname) for fname in functions_to_remove
    ]

    cut = [[zeroAddress, facetCutAction["Remove"], selectors_to_remove]]

    # Cut the Diamond
    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )
    function_selectors = diamondLoupe.facetFunctionSelectors(test1.address)
    assert len(function_selectors) == 15
    for fsr in selectors_to_remove:
        if fsr in function_selectors:
            assert False


def test_remove_all_facets_and_functions_except_diamondcut_and_facets(
    accounts, contracts
):
    owner = accounts[0]
    diamondCut = contracts[1]
    diamondLoupe = contracts[2]
    
    # get all the selectors
    facets_with_selectors = diamondLoupe.facets()
    all_selectors = []
    for x in facets_with_selectors:
        all_selectors.extend(list(x[1]))
    
    # remove ['facets()', 'diamondCut((address,uint8,bytes4[])[],address,bytes)']) from selectors
    selectors_to_keep = [
        hashFunctionSignature('facets()'),
        hashFunctionSignature('diamondCut((address,uint8,bytes4[])[],address,bytes)')
    ]

    for s in selectors_to_keep:
        all_selectors.remove(s)

    # Cut the Diamond
    cut = [[zeroAddress, facetCutAction["Remove"], all_selectors]]

    # Cut the Diamond
    diamondCut.diamondCut(
        cut, zeroAddress, bytes(0), {"from": owner, "gasLimit": 800000}
    )

    facets = diamondLoupe.facets()
    
    assert len(facets) == 2

@pytest.mark.skip
def test_add_most_functions_and_facets(accounts, contracts):
    diamondLoupe = contracts[2]
    diamondLoupeSelectors = getSelectors(diamondLoupe)

    for function_name in ['supportsInterface(bytes4)', 'facets()']:
        diamondLoupeSelectors.remove(hashFunctionSignature(function_name))

