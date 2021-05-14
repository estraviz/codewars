import pytest

from solution import small_enough


data = [
    ([66, 101], 200, True),
    ([78, 117, 110, 99, 104, 117, 107, 115], 100, False),
    ([101, 45, 75, 105, 99, 107], 107, True),
    ([80, 117, 115, 104, 45, 85, 112, 115], 120, True),
    ([1, 1, 1, 1, 1, 2], 1, False),
    ([78, 33, 22, 44, 88, 9, 6], 87, False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, True),
    ([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12, True),
]


@pytest.mark.parametrize(
    "array, limit, expected", data
)
def test_small_enought(array, limit, expected):
    assert small_enough(array, limit) == expected
