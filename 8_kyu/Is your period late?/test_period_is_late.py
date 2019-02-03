from period_is_late import period_is_late
from datetime import date


def test_period_is_late():
    assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35) is False
    assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28) is True
    assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35) is False
    assert period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28) is False
    assert period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28) is False
    assert period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28) is True
    assert period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30) is True
    assert period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30) is False
    assert period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30) is False
    assert period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30) is True
