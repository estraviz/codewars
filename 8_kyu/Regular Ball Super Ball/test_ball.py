from ball import Ball


def test_regular_ball():
    assert Ball().ball_type == "regular"


def test_super_ball():
    assert Ball('super').ball_type == "super"
