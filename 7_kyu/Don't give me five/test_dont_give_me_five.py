from dont_give_me_five import dont_give_me_five


def test_basic_tests():
    assert dont_give_me_five(1, 9) == 8
    assert dont_give_me_five(4, 17) == 12


def test_more_tests():
    assert dont_give_me_five(1, 90) == 72
    assert dont_give_me_five(-4, 17) == 20
    assert dont_give_me_five(-4, 37) == 38
    assert dont_give_me_five(-14, -1) == 13
    assert dont_give_me_five(-14, -6) == 9
