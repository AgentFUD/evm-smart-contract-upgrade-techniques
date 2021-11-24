import web3

facetCutAction = {"Add": 0, "Replace": 1, "Remove": 2}

zeroAddress = "0x0000000000000000000000000000000000000000"


def getSelectors(contract):
    return list(contract.signatures.values())


def hashFunctionSignature(function_signature_text):
    return web3.Web3.keccak(text=function_signature_text).hex()[0:10]
