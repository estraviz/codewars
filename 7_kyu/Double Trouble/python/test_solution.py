import pytest

from solution import trouble


TESTS = [
    [([1, 3, 5, 6, 7, 4, 3], 7), [1, 3, 5, 6, 7, 4]],
    [([4, 1, 1, 1, 4], 2), [4, 1, 4]],
    [([2, 6, 2], 8), [2, 2]],
    [([2, 2, 2, 2, 2, 2], 4), [2]],
]


@pytest.mark.parametrize(
    "inp, expected", TESTS
)
def test_trouble(inp, expected):
    assert trouble(*inp) == expected
