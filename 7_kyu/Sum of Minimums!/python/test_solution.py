import pytest

from solution import sum_of_minimums


data = [
    ([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ], 9),
    ([ [11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]], 76),
]


@pytest.mark.parametrize(
    "numbers, expected", data
)
def test_sum_of_minimums(numbers, expected):
    assert sum_of_minimums(numbers) == expected
