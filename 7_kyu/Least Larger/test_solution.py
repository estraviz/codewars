import pytest
from solution import least_larger


@pytest.mark.parametrize(
    "arr, ind, result",
    [([4, 1, 3, 5, 6], 0, 3), ([4, 1, 3, 5, 6], 4, -1), ([1, 3, 5, 2, 4], 0, 3)],
)
def test_least_larger_with_example_tests(arr, ind, result):
    assert least_larger(arr, ind) == result


@pytest.mark.parametrize(
    "arr, ind, result",
    [
        ([1, 2, 3, 4, 5, 0], 5, 0),
        ([1, 2, 3, 4, 5, 0], 0, 1),
        ([1, 2, 3, 4, 5, 0], 1, 2),
        ([1, 2, 3, 4, 5, 0], 2, 3),
        ([1, 2, 3, 4, 5, 0], 3, 4),
        ([1, 2, 3, 4, 5, 0], 4, -1),
        ([0], 0, -1),
        ([0, 0], 1, -1),
    ],
)
def test_least_larger_with_fixed_tests(arr, ind, result):
    assert least_larger(arr, ind) == result
