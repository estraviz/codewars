import pytest

from solution import remainder


tests = [
    (3, 2, 1),
    (19, 2, 1),
    (10, 2, 0),
    (34, 7, 6),
    (27, 5, 2),
]


@pytest.mark.parametrize(
    "dividend, divisor, expected", tests
)
def test_remainder(dividend, divisor, expected):
    assert remainder(dividend, divisor) == expected
