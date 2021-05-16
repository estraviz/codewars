import pytest

from solution import largest_pair_sum


data = [
    ([10, 14, 2, 23, 19], 42),
    ([-100, -29, -24, -19, 19], 0),
    ([1, 2, 3, 4, 6, -1, 2], 10),
    ([-10, -8, -16, -18, -19], -18),
]


@pytest.mark.parametrize(
    "numbers, expected", data
)
def test_largest_pair_sum(numbers, expected):
    assert largest_pair_sum(numbers) == expected
