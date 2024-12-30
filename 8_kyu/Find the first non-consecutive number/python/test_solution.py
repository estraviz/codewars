import pytest

from solution import first_non_consecutive

data = [
    ([1, 2, 3, 4, 6, 7, 8], 6),
    ([1, 2, 3, 4, 5, 6, 7, 8], None),
    ([4, 6, 7, 8, 9, 11], 6),
    ([4, 5, 6, 7, 8, 9, 11], 11),
    ([31, 32], None),
    ([-3, -2, 0, 1], 0),
    ([-5, -4, -3, -1], -1),
]

@pytest.mark.parametrize(
    "arr, expected", data
)
def test_first_non_consecutive(arr, expected):
    assert first_non_consecutive(arr) == expected
