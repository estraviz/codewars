from fraction import fraction


def test_fraction():
    assert fraction(90, 120) == 7
    assert fraction(2, 4) == 3
    assert fraction(100, 1000) == 11
    assert fraction(3, 15) == 6
    assert fraction(114, 200) == 157
    assert fraction(3, 118) == 121
