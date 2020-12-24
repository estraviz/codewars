import pytest

from solution import solve


@pytest.mark.parametrize(
    "arr, result",
    [
        ([3, 4, 4, 3, 6, 3], [4, 6, 3]),
        ([1, 2, 1, 2, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 1, 4, 5, 1, 2, 1], [4, 5, 2, 1]),
    ],
)
def test_solve(arr, result):
    assert solve(arr) == result
