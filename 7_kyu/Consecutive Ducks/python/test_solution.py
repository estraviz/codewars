from solution import consecutive_ducks


def test_check_small_values():
    assert consecutive_ducks(69) is True
    assert consecutive_ducks(8) is False
    assert consecutive_ducks(57) is True
    assert consecutive_ducks(6) is True
    assert consecutive_ducks(13) is True
    assert consecutive_ducks(16) is False
    assert consecutive_ducks(91) is True
    assert consecutive_ducks(75) is True
    assert consecutive_ducks(38) is True
    assert consecutive_ducks(25) is True
    assert consecutive_ducks(32) is False
    assert consecutive_ducks(65) is True
    assert consecutive_ducks(13) is True
    assert consecutive_ducks(16) is False
    assert consecutive_ducks(99) is True


def test_check_medium_values():
    assert consecutive_ducks(522) is True
    assert consecutive_ducks(974) is True
    assert consecutive_ducks(755) is True
    assert consecutive_ducks(512) is False
    assert consecutive_ducks(739) is True
    assert consecutive_ducks(1006) is True
    assert consecutive_ducks(838) is True
    assert consecutive_ducks(1092) is True
    assert consecutive_ducks(727) is True
    assert consecutive_ducks(648) is True
    assert consecutive_ducks(1024) is False
    assert consecutive_ducks(851) is True
    assert consecutive_ducks(541) is True
    assert consecutive_ducks(1011) is True
    assert consecutive_ducks(822) is True


def test_check_large_values():
    assert consecutive_ducks(382131) is True
    assert consecutive_ducks(118070) is True
    assert consecutive_ducks(17209) is True
    assert consecutive_ducks(32768) is False
    assert consecutive_ducks(161997) is True
    assert consecutive_ducks(400779) is True
    assert consecutive_ducks(198331) is True
    assert consecutive_ducks(325482) is True
    assert consecutive_ducks(88441) is True
    assert consecutive_ducks(648) is True
    assert consecutive_ducks(65536) is False
    assert consecutive_ducks(323744) is True
    assert consecutive_ducks(183540) is True
    assert consecutive_ducks(65271) is True
    assert consecutive_ducks(5263987) is True
