import pytest

from solution import fold_array


arr = [1, 2, 3, 4, 5]

basic_tests = [
    [[arr, 1], [6, 6, 3]],
    [[arr, 2], [9, 6]],
    [[arr, 3], [15]],
    [[[-9, 9, -8, 8, 66, 23], 1], [14, 75, 0]],
]


@pytest.mark.parametrize(
    "inp, expected", basic_tests
)
def test_fold_array_basic(inp, expected):
    assert fold_array(*inp) == expected


extended_tests = [
    [[1, 2, 3, 4, 5, 99, 88, 78, 74, 73], 5],
    [[-1, -2, -3, -4, -5, -99, -88, -78, -74, -73], 5],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10],
    [[2], 1],
    [[2], 200],
]


@pytest.mark.parametrize(
    "array, runs", extended_tests
)
def test_fold_array_extended(array, runs):
    assert fold_array(array, runs) == [sum(array)]
