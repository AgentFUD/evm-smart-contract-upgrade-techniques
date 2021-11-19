import brownie


def test_storage_keeps_values_if_switched_to_v2(social_site_contract_v2):
    orig = social_site_contract_v2[0]
    updated = social_site_contract_v2[1]

    orig.like("https://orno.io/article")
    orig.disLike("https://myblog.io/article")

    assert orig.getLikes("https://orno.io/article") == 1
    assert updated.getLikes("https://orno.io/article") == 1

    assert orig.getDisLikes("https://myblog.io/article") == 1
    assert updated.getDisLikes("https://myblog.io/article") == 1


def test_v2_only_allows_like_once(social_site_contract_v2):
    orig = social_site_contract_v2[0]
    updated = social_site_contract_v2[1]

    updated.like("https://orno.io/article")

    assert orig.getLikes("https://orno.io/article") == 2
    assert updated.getLikes("https://orno.io/article") == 2

    with brownie.reverts("ERROR: User has already liked"):
        updated.like("https://orno.io/article")


def test_v2_only_allows_dislike_once(social_site_contract_v2):
    orig = social_site_contract_v2[0]
    updated = social_site_contract_v2[1]

    assert orig.getDisLikes("https://myblog.io/article") == 1
    assert updated.getDisLikes("https://myblog.io/article") == 1

    updated.disLike("https://myblog.io/article")

    with brownie.reverts("ERROR: User has already disliked"):
        updated.disLike("https://myblog.io/article")
