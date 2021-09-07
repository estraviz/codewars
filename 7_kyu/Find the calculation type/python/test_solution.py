import pytest

from solution import calc_type


tests = [
    (1, 2, 3, "addition"),
    (10, 5, 5, "subtraction"),
    (10, 4, 40, "multiplication"),
    (9, 5, 1.8, "division"),
]


@pytest.mark.parametrize(
    "a, b, res, expected", tests
)
def test_calc_type(a, b, res, expected):
    assert calc_type(a, b, res) == expected
