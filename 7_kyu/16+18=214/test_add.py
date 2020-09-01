from add import add


def test_real_addition_test():
    assert add(2, 11) == 13
    assert add(0, 1) == 1
    assert add(0, 0) == 0


def test_silly_addition_test():
    assert add(16, 18) == 214
    assert add(26, 39) == 515
    assert add(122, 81) == 1103


def test_silly_big_addition():
    assert add(1222, 30277) == 31499
    assert add(1236, 30977) == 31111013
    assert add(38810, 1383) == 391193
