import pytest

from solution import strange_math


basic_tests = [
    (11, 2, 4),
    (15, 5, 11),
    (15, 15, 7),
]


@pytest.mark.parametrize(
    "n, k, expected", basic_tests
)
def test_basic_strange_math(n, k, expected):
    assert strange_math(n, k) == expected
