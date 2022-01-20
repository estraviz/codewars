import pytest

from solution import odd_or_even


tests = [
    (1, "Either"),
    (3, "Either"),
    (6, "Odd"),
    (8, "Even"),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_odd_or_even(n, expected):
    assert odd_or_even(n) == expected
