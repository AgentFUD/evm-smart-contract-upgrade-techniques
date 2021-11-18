// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "./SocialLib.sol";

contract SocialSite {
    using SocialLib for address;
    address eternalStorage;

    constructor(address _eternalStorage) {
        eternalStorage = _eternalStorage;
    }

    function like(string memory _url) public {
        eternalStorage.likeURL(_url);
    }

    function disLike(string memory _url) public {
        eternalStorage.disLikeURL(_url);
    }

    function getLikes(string memory _url) public view returns(uint256) {
        return eternalStorage.getLikesOfURL(_url);
    }
    
    function getDisLikes(string memory _url) public view returns(uint256) {
        return eternalStorage.getDisLikesOfURL(_url);
    }
}