import pytest

from solution import my_parse_int


data = [
    ("1", 1),
    ("  1 ", 1),
    ("08", 8),
    ("5 friends", "NaN"),
    ("16.5", "NaN"),
]


@pytest.mark.parametrize("s, result", data)
def test_my_parse_int_basic_cases(s, result):
    assert my_parse_int(s) == result


def test_my_parse_int_should_parse_integers_properly():
    for i in range(20):
        assert my_parse_int(str(i)) == i


def test_my_parse_int_should_parse_number_starting_with_properly():
    for i in range(10):
        assert my_parse_int("0" + str(i)) == i
        assert my_parse_int("00" + str(i)) == i


more_data = [
    ("5 friends", "NaN"),
    ("5friends", "NaN"),
    ("I <3 u", "NaN"),
    ("17.42", "NaN"),
    ("0x10", "NaN"),
    ("123~~", "NaN"),
    ("1 1", "NaN"),
    ("1 2 3", "NaN"),
    ("1.0", "NaN"),
]


@pytest.mark.parametrize("s, result", more_data)
def test_my_parse_int_should_return_NaN_for_non_integer_strings(s, result):
    assert my_parse_int(s) == result
