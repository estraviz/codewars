from get_ages import get_ages


def test_get_ages_good_values():
    assert get_ages(24, 4) == (14, 10)
    assert get_ages(24, 4) == (14, 10)
    assert get_ages(30, 6) == (18, 12)
    assert get_ages(70, 10) == (40, 30)
    assert get_ages(18, 4) == (11, 7)
    assert get_ages(63, 14) == (38.5, 24.5)
    assert get_ages(80, 80) == (80, 0)


def test_get_ages_bad_values():
    assert get_ages(63, -14) is None
    assert get_ages(63, -14) is None
    assert get_ages(-22, 15) is None
