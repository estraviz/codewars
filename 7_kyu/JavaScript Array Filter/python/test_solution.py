import pytest

from solution import get_even_numbers


data = [
    ([2, 4, 5, 6], [2, 4, 6]),
    ([], []),
    ([1], []),
    ([1, 2], [2]),
    ([1, 2, 3, 4, 5], [2, 4]),
    ([2, 4, 6, 8], [2, 4, 6, 8]),
]


@pytest.mark.parametrize(
    "arr, expected", data
)
def test_get_even_numbers(arr, expected):
    assert get_even_numbers(arr) == expected
