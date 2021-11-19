import brownie


def test_we_can_like_an_url(social_site_contract):
    social_site_contract.like("https://orno.io")
    social_site_contract.like("https://orno.io")
    social_site_contract.like("https://orno.io")
    social_site_contract.like("https://orno.io")

    num_likes = social_site_contract.getLikes("https://orno.io")

    assert num_likes == 4

    assert social_site_contract.getLikes("https://youtube.com") == 0


def test_we_can_dislike_an_url(social_site_contract):
    social_site_contract.disLike("https://youtube.com")
    social_site_contract.disLike("https://youtube.com")
    social_site_contract.disLike("https://youtube.com")

    assert social_site_contract.getDisLikes("https://youtube.com") == 3


def test_we_can_mix_likes_and_dislikes(social_site_contract):
    likes = social_site_contract.getLikes("https://orno.io")
    disLikes = social_site_contract.getDisLikes("https://orno.io")

    social_site_contract.like("https://orno.io")
    social_site_contract.like("https://orno.io")
    social_site_contract.disLike("https://orno.io")
    social_site_contract.disLike("https://orno.io")
    social_site_contract.like("https://orno.io")
    social_site_contract.like("https://orno.io")

    assert social_site_contract.getLikes("https://orno.io") == likes + 4
    assert social_site_contract.getDisLikes("https://orno.io") == disLikes + 2


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
