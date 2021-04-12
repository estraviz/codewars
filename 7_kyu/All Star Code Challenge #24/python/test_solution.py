from solution import hypotenuse, leg


def test_hypotenuse_and_leg():
    assert hypotenuse(4, 3) == 5
    assert leg(5, 3) == 4
