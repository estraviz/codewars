import pytest

from solution import highest_rank


tests = [
    ([12, 10, 8, 12, 7, 6, 4, 10, 12], 12),
    ([12, 10, 8, 12, 7, 6, 4, 10, 10], 10),
    ([12, 10, 8, 12, 7, 6, 4, 10, 12, 10], 12),
    ([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10], 3),
    ([1, 2, 3], 3),
    ([1, 1, 2, 3], 1),
    ([1, 1, 2, 2, 3], 2),
]


@pytest.mark.parametrize(
    "arr, expected", tests
)
def test_should_return_highest_rank_number_in_array(arr, expected):
    assert highest_rank(arr) == expected
