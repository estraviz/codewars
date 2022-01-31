import pytest

from solution import solve


tests = [
    ([2, 7, 5, 9, 100, 34, 32, 0], 3, [4, 8, 7, 9, 101, 35, 34, 0]),
    ([1000, 999, 998, 997], 5, [1000, 1003, 1001, 999]),
    ([], 2, []),
    ([0, 0, 0, 0], 5, [0, 0, 0, 0]),
    ([4, 3, 2, 1], 5, [8, 6, 4, 2]),
    ([33, 23, 45, 78, 65], 10, [36, 26, 50, 86, 70]),
    (list(range(1, 99)), 11, [x + x % 11 for x in list(range(1, 99))]),
    (list(range(1, 9999)), 3658, [x + x % 3658 for x in list(range(1, 9999))]),
]


@pytest.mark.parametrize(
    "nums, div, expected", tests
)
def test_solve(nums, div, expected):
    assert solve(nums, div) == expected
