import pytest

from solution import is_sorted_and_how


data = [
    ([1, 2], 'yes, ascending'),
    ([15, 7, 3, -8], 'yes, descending'),
    ([4, 2, 30], 'no'),
]


@pytest.mark.parametrize(
    "arr, expected", data
)
def test_is_sorted_and_how(arr, expected):
    assert is_sorted_and_how(arr) == expected
