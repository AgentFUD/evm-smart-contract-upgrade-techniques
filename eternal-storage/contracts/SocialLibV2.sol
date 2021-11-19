// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "./EternalStorage.sol";

library SocialLibV2 {
    
    // likes
    function likeURL(address _eternalStorage, string memory _url) public {
        uint256 currentLikes = getLikesOfURL(_eternalStorage, _url);
        bytes32 slot = keccak256(abi.encodePacked(_url, 'likes'));
        EternalStorage(_eternalStorage).setUintValue(slot, currentLikes + 1);
    }

    function getLikesOfURL(address _eternalStorage, string memory _url) public view returns(uint256) {
        bytes32 slot = keccak256(abi.encodePacked(_url, 'likes'));
        return EternalStorage(_eternalStorage).getUIntValue(slot);
    }

    function setUserHasLikedURL(address _eternalStorage, string memory _url) public {
        bytes32 slot = keccak256(abi.encodePacked(_url, 'likes', msg.sender));
        EternalStorage(_eternalStorage).setBoolValue(slot, true);
    }

    function getUserHasLikedURL(address _eternalStorage, string memory _url) public view returns(bool) {
        bytes32 slot = keccak256(abi.encodePacked(_url, 'likes', msg.sender));
        return EternalStorage(_eternalStorage).getBoolValue(slot);
    }

    // dislikes
    function disLikeURL(address _eternalStorage, string memory _url) public {
        uint256 currentDisLikes = getDisLikesOfURL(_eternalStorage, _url);
        bytes32 slot = keccak256(abi.encodePacked(_url, 'dislikes'));
        EternalStorage(_eternalStorage).setUintValue(slot, currentDisLikes + 1);
    }

    function getDisLikesOfURL(address _eternalStorage, string memory _url) public view returns(uint256) {
        bytes32 slot = keccak256(abi.encodePacked(_url, 'dislikes'));
        return EternalStorage(_eternalStorage).getUIntValue(slot);
    }

    function setUserHasDisLikedURL(address _eternalStorage, string memory _url) public {
        bytes32 slot = keccak256(abi.encodePacked(_url, 'dislikes', msg.sender));
        EternalStorage(_eternalStorage).setBoolValue(slot, true);
    }

    function getUserHasDisLikedURL(address _eternalStorage, string memory _url) public view returns(bool) {
        bytes32 slot = keccak256(abi.encodePacked(_url, 'dislikes', msg.sender));
        return EternalStorage(_eternalStorage).getBoolValue(slot);
    }
}