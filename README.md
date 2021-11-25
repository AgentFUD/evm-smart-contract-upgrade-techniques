# evm-smart-contract-upgrade-techniques
Simple eth-brownie projects to demonstrate different smart contract upgrade techniques

To see how they work first install  [eth-brownie](https://github.com/eth-brownie/brownie), then clone the repository. After that enter directories and run ***brownie test -v*** By examining the tests you can get an idea how to work with these upgrade techniques.

## [Ancient Proxy](ancient-proxy)
This is a modernized implementation of [Nick Johnson](https://gist.github.com/Arachnid)'s [upgradeable.sol](https://gist.github.com/Arachnid/4ca9da48d51e23e5cfe0f0e14dd6318f), the grandfather of all the upgradeability/proxy patterns. 

## [Eternal Storage](eternal-storage)
Based on a [blog post](https://medium.com/colony/writing-upgradeable-contracts-in-solidity-6743f0eecc88) of [Elena Gesheva](https://medium.com/@elena_gesheva)

## Diamond Pattern eip-2535

These are examples of [Nick Mudge](https://github.com/mudgen) [eip-2535](https://eips.ethereum.org/EIPS/eip-2535) diamond reference implementation with [eth-brownie](https://github.com/eth-brownie/brownie) for python lovers. In the three diamond directory the tests are the same, smart contracts are different. 

[diamond-1-brownie](diamond-1-brownie) 

[diamond-2-brownie](diamond-2-brownie) 

[diamond-3-brownie](diamond-3-brownie) 

To see gas consumption, run ***brownie test --gas*** in each diamond directory.