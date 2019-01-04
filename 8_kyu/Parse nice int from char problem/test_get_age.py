from get_age import get_age


def test_get_age():
    assert get_age("1 year old") == 1
    assert get_age("2 years old") == 2
    assert get_age("3 years old") == 3
    assert get_age("4 years old") == 4
    assert get_age("5 years old") == 5
    assert get_age("6 years old") == 6
    assert get_age("7 years old") == 7
    assert get_age("8 years old") == 8
    assert get_age("9 years old") == 9
