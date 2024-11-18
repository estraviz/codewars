from set_alarm import set_alarm


def test_set_alarm():
    assert set_alarm(True, True) is False
    assert set_alarm(False, True) is False
    assert set_alarm(False, False) is False
    assert set_alarm(True, False) is True
