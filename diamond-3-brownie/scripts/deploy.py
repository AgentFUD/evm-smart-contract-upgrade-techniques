from brownie import Contract, accounts
from brownie import (
    Diamond,
    DiamondCutFacet,
    DiamondLoupeFacet,
    OwnershipFacet,
    DiamondInit,
)

# from brownie import Test1Facet, Test2Facet
from scripts.helpers import facetCutAction, getSelectors


def main():
    owner = accounts[0]

    diamondCutFacet = DiamondCutFacet.deploy({"from": owner})
    diamondLoupeFacet = DiamondLoupeFacet.deploy({"from": owner})
    ownershipFacet = OwnershipFacet.deploy({"from": owner})
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
    initSelector = getSelectors(DiamondInit)

    diamondCut.diamondCut(cut, diamondInit.address, initSelector[0], {"from": owner})
