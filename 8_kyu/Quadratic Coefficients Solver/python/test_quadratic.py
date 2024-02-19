from quadratic import quadratic


def test_basic():
    assert quadratic(0, 1) == (1, -1, 0)
    assert quadratic(4, 9) == (1, -13, 36)
    assert quadratic(2, 6) == (1, -8, 12)
    assert quadratic(-5, -4) == (1, 9, 20)
