import pytest

from solution import averages


tests = (
    ([2, 2, 2, 2], [2, 2, 2, 2, 2]),
    ([0, 0, 0, 0], [2, -2, 2, -2, 2]),
    ([2, 4, 3, -4.5], [1, 3, 5, 1, -10]),
    ([], []),
    ([], [1]),
    ([], None),
)


@pytest.mark.parametrize(
    "expected, arr", tests
)
def test_averages(expected, arr):
    assert averages(arr) == expected
