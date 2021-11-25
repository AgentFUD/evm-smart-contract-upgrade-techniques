# evm-smart-contract-upgrade-techniques
Simple eth-brownie projects to demonstrate different smart contract upgrade techniques

To see how they work first install  [eth-brownie](https://github.com/eth-brownie/brownie), then clone the repository. After that enter directories and run ***brownie test -v*** By examining the tests you can get an idea how to work with these upgrade techniques.

## Ancient Proxy

## Eternal Storage

## Diamond Pattern eip-2535

These are examples of [Nick Mudge](https://github.com/mudgen) [eip-2535](https://eips.ethereum.org/EIPS/eip-2535) diamond reference implementation with [eth-brownie](https://github.com/eth-brownie/brownie) for python lovers. The smart contracts run against the same tests.

[diamond-1-brownie](diamond-1-brownie) 

[diamond-2-brownie](diamond-2-brownie) 

[diamond-3-brownie](diamond-3-brownie) 

To see gas consumption, run ***brownie test --gas*** in each diamond directory.