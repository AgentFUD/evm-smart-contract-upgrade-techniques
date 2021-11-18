// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

contract EternalStorage {

    mapping(bytes32 => uint256) internal uintStorage;
    mapping(bytes32 => string) internal stringStorage;
    mapping(bytes32 => address) internal addressStorage;
    mapping(bytes32 => bytes) internal bytesStorage;
    mapping(bytes32 => bool) internal boolStorage;
    mapping(bytes32 => int256) internal intStorage;

    function getUIntValue(bytes32 record) public view returns (uint) {
        return uintStorage[record];
    }

    function setUintValue(bytes32 record, uint256 value) public {
        uintStorage[record] = value;
    }

    function getStringValue(bytes32 record) public view returns (string memory) {
        return stringStorage[record];
    }

    function setStringValue(bytes32 record, string memory value) public {
        stringStorage[record] = value;
    }

    function getAddressValue(bytes32 record) public view returns (address) {
        return addressStorage[record];
    }

    function setAddressValue(bytes32 record, address value) public {
        addressStorage[record] = value;
    }

    function getBytesValue(bytes32 record) public view returns (bytes memory) {
        return bytesStorage[record];
    }

    function setBytesValue(bytes32 record, bytes memory value) public {
        bytesStorage[record] = value;
    }

    function getBoolValue(bytes32 record) public view returns (bool) {
        return boolStorage[record];
    }

    function setBoolValue(bytes32 record, bool value) public {
        boolStorage[record] = value;
    }

    function getIntValue(bytes32 record) public view returns (int256) {
        return intStorage[record];
    }

    function setIntValue(bytes32 record, int256 value) public {
        intStorage[record] = value;
    }
}