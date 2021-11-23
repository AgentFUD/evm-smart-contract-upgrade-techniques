// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

abstract contract Upgradeable {

    mapping(bytes4 => uint32) _sizes;

    address destination;

    function initialize() virtual public ;

    function replace(address _destination) public {
        destination = _destination;
        _destination.delegatecall(abi.encodeWithSelector(bytes4(keccak256("initialize()"))));
    }
}
