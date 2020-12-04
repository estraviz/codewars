import pytest

from solution import sum_square_even_root_odd


@pytest.mark.parametrize(
    "nums, result", [([4, 5, 7, 8, 1, 2, 3, 0], 91.61), ([1, 14, 9, 8, 17, 21], 272.71)]
)
def test_sum_square_even_root_odd(nums, result):
    assert sum_square_even_root_odd(nums) == result
