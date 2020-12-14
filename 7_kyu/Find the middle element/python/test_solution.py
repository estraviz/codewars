import pytest

from solution import gimme


@pytest.mark.parametrize(
    "arr, ind",
    [
        ([2, 3, 1], 0),
        ([5, 10, 14], 1),
        ([1, 3, 4], 1),
        ([15, 10, 14], 2),
        ([-0.410, -23, 4], 0),
        ([-15, -10, 14], 1),
    ],
)
def test_gimme(arr, ind):
    assert gimme(arr) == ind
