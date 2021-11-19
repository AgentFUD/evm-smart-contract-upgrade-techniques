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
