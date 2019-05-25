from break_chocolate import break_chocolate


def test_break_chocolate():
    assert break_chocolate(5, 5) == 24
    assert break_chocolate(7, 4) == 27
    assert break_chocolate(1, 1) == 0
    assert break_chocolate(0, 0) == 0
    assert break_chocolate(6, 1) == 5
