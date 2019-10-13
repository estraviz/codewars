from get_ages import get_ages


def test_get_ages():
    assert get_ages(24, 4) == (14, 10)
    assert get_ages(63, -14) is None
