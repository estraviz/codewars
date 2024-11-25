import pytest

from solution import derive

data = [
    (7, 8, "56x^7"),
    (5, 9, "45x^8"),
]


@pytest.mark.parametrize(
    "coefficient, exponent, expected", data)
def test_example_tests(coefficient, exponent, expected):
    assert derive(coefficient, exponent) == expected
