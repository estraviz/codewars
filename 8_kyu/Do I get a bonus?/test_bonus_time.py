from bonus_time import bonus_time


def test_bonus_time():
    assert bonus_time(10000, True) == '$100000'
    assert bonus_time(25000, True) == '$250000'
    assert bonus_time(10000, False) == '$10000'
    assert bonus_time(60000, False) == '$60000'
    assert bonus_time(2, True) == '$20'
    assert bonus_time(78, False) == '$78'
