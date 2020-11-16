import pytest
from solution import sum_arrays


@pytest.mark.parametrize(
    "array1, array2, result",
    [
        [[3, 2, 9], [1, 2], [3, 4, 1]],
        [[4, 7, 3], [1, 2, 3], [5, 9, 6]],
        [[1], [5, 7, 6], [5, 7, 7]],
        [[3, 2, 6, 6], [-7, 2, 2, 8], [-3, 9, 6, 2]],
        [[-4, 5, 7, 3, 6], [5, 3, 4, 5], [-4, 0, 3, 9, 1]],
        [[-3, 4, 2], [3, 4, 4], [2]],
    ],
)
def test_sum_arrays_basic(array1, array2, result):
    assert sum_arrays(array1, array2) == result


@pytest.mark.parametrize(
    "array1, array2, result",
    [
        [[], [], []],
        [[0], [], [0]],
        [[], [1, 2], [1, 2]],
        [[1, 4, 5], [], [1, 4, 5]],
        [[0], [0], [0]],
    ],
)
def test_sum_arrays_empty(array1, array2, result):
    assert sum_arrays(array1, array2) == result
