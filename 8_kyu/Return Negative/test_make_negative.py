from make_negative import make_negative


def test_make_negative():
    assert make_negative(42) == -42
    assert make_negative(-9) == -9
    assert make_negative(0) == 0
    assert make_negative(1) == -1
    assert make_negative(-1) == -1
