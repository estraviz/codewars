from double_integer import double_integer


def test_double_integer():
    assert double_integer(2) == 4
    assert double_integer(4) == 8
    assert double_integer(-10) == -20
    assert double_integer(0) == 0
    assert double_integer(100) == 200
