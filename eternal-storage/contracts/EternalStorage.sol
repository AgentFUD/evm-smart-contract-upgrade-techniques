// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

contract EternalStorage {

    mapping(bytes32 => uint256) internal uintStorage;
    mapping(bytes32 => bool) internal boolStorage;

    function getUIntValue(bytes32 record) public view returns (uint) {
        return uintStorage[record];
    }

    function setUintValue(bytes32 record, uint256 value) public {
        uintStorage[record] = value;
    }

    function getBoolValue(bytes32 record) public view returns (bool) {
        return boolStorage[record];
    }

    function setBoolValue(bytes32 record, bool value) public {
        boolStorage[record] = value;
    }
}