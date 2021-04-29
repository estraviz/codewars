import pytest

from solution import find_longest


data = [
    ([1, 10, 100], 100),
    ([9000, 8, 800], 9000),
    ([8, 900, 500], 900),
    ([3, 40000, 100], 40000),
    ([1, 200, 100000], 100000),
]


@pytest.mark.parametrize(
    "arr, expected", data
)
def test_find_longest(arr, expected):
    assert find_longest(arr) == expected
