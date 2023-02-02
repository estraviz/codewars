from datetime import datetime

from solution import is_today


def test_sample_tests():
    assert is_today(datetime(2020, 10, 1, 1, 1, 1, 1)) is False
    assert is_today(datetime(2080, 10, 1, 1, 1, 1, 1)) is False
    assert is_today(datetime.today()) is True
