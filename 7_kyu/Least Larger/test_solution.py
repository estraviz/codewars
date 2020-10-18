import pytest
from solution import least_larger


@pytest.mark.parametrize(
    "arr, ind, result",
    [([4, 1, 3, 5, 6], 0, 3),
     ([4, 1, 3, 5, 6], 4, -1),
     ([1, 3, 5, 2, 4], 0, 3)]
)
def test_least_larger(arr, ind, result):
    assert least_larger(arr, ind) == result
