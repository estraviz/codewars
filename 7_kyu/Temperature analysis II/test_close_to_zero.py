from close_to_zero import close_to_zero


def test_close_to_zero():
    assert close_to_zero('') == 0
    assert close_to_zero('-1 50 -4 20 22 -7 0 10 -8') == 0
    assert close_to_zero('28 35 -21 17 38 -17') == 17
