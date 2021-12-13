import pytest

from solution import digits


tests = [
    (0, 1),
    (1, 1),
    (5, 1),
    (9, 1),
    (10, 2),
    (11, 2),
    (99, 2),
    (100, 3),
    (101, 3),
    (12345, 5),
    (9876543210, 10),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_digits(n, expected):
    assert digits(n) == expected
