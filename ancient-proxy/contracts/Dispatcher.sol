// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "./Upgradeable.sol";

contract Dispatcher is Upgradeable {

    constructor(address target) {
        replace(target);
    }

    function initialize() override public pure {
        // Should only be called by on target contracts, not on the dispatcher
        assert(false);
    }

    fallback() external {
        bytes4 sig;
        assembly { sig := calldataload(0) }
        uint len = _sizes[sig];
        address target = destination;

        assembly {
            calldatacopy(0x0, 0x0, calldatasize())
            let result := delegatecall(sub(gas(), 10000), target, 0x0, calldatasize(), 0, len)
            return(0, len) //we throw away any return data
        }
    }
}
