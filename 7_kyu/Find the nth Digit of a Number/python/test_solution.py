import pytest

from solution import find_digit


@pytest.mark.parametrize(
    "num, nth, expected",
    [
        (5673, 4, 5),
        (129, 2, 2),
        (-2825, 3, 8),
        (0, 20, 0),
        (65, 0, -1),
        (24, -8, -1),
    ]
)
def test_should_return_correct_for_normal_values(num, nth, expected):
    assert find_digit(num, nth) == expected


@pytest.mark.parametrize(
    "num, nth, expected",
    [
        (-456, 5, 0),
        (-1234, 2, 3),
        (-5540, 1, 0),
    ]
)
def test_should_return_correctly_for_negative_values(num, nth, expected):
    assert find_digit(num, nth) == expected


@pytest.mark.parametrize(
    "num, nth, expected",
    [
        (678998, 0, -1),
        (-67854, -57, -1),
        (0, -3, -1),
    ]
)
def test_should_return_correctly_when_nth_is_not_positive(num, nth, expected):
    assert find_digit(num, nth) == expected
