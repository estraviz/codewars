from how_much_i_love_you import how_much_i_love_you


def test_how_much_i_love_you():
    assert how_much_i_love_you(7) == "I love you"
    assert how_much_i_love_you(3) == "a lot"
    assert how_much_i_love_you(6) == "not at all"
