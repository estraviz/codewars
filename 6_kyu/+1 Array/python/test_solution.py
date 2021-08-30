import pytest

from solution import up_array


tests_basic_tests = [
    ([2, 3, 9],  [2, 4, 0]),
    ([4, 3, 2, 5],  [4, 3, 2, 6]),
    ([5, 7, 4],  [5, 7, 5]),
    ([0],  [1]),
    ([1, 0, 0, 0],  [1, 0, 0, 1]),
    ([9, 9, 9],  [1, 0, 0, 0]),
    ([2,  1,  4,  7,  4,  8,  3,  6,  4,  7],  [2,  1,  4,  7,  4,  8,  3,  6,  4,  8]),
]


@pytest.mark.parametrize(
    "arr,  expected", tests_basic_tests
)
def test_basic_tests(arr,  expected):
    assert up_array(arr) == expected


tests_invalid_array = [
    ([1, -9],  None),
    ([1, 2, 33],  None),
    ([1, 2, -1],  None),
    ([10],  None),
#([3.14,  1.41,  2.72],  None),
    ([],  None),
]


@pytest.mark.parametrize(
    "arr,  expected",  tests_invalid_array
)
def test_invalid_array(arr,  expected):
    assert up_array(arr) == expected


tests_big_arrays = [
    ([9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 7],
     [9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 8]),
    ([9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 7, 5, 3, 2, 6, 7,
      8, 4, 2, 4, 2, 6, 7, 8, 7, 4, 5, 2, 1],
     [9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 7, 5, 3, 2, 6, 7,
      8, 4, 2, 4, 2, 6, 7, 8, 7, 4, 5, 2, 2]),
]


@pytest.mark.parametrize(
    "arr,  expected",  tests_big_arrays
)
def test_big_arrays(arr,  expected):
    assert up_array(arr) == expected
