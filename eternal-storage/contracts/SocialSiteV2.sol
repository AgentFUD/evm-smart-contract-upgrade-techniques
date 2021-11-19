// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "./SocialLibV2.sol";

contract SocialSiteV2 {
    
    using SocialLibV2 for address;
    address eternalStorage;

    constructor(address _eternalStorage) {
        eternalStorage = _eternalStorage;
    }

    function like(string memory _url) public {
        require(eternalStorage.getUserHasLikedURL(_url) == false, "ERROR: User has already liked");
        eternalStorage.setUserHasLikedURL(_url);
        eternalStorage.likeURL(_url);
    }

    function disLike(string memory _url) public {
        require(eternalStorage.getUserHasDisLikedURL(_url) == false, "ERROR: User has already disliked");
        eternalStorage.setUserHasDisLikedURL(_url);
        eternalStorage.disLikeURL(_url);
    }

    function getLikes(string memory _url) public view returns(uint256) {
        return eternalStorage.getLikesOfURL(_url);
    }
    
    function getDisLikes(string memory _url) public view returns(uint256) {
        return eternalStorage.getDisLikesOfURL(_url);
    }
}