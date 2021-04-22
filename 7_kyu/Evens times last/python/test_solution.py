import pytest

from solution import even_last


data = [
    ([2, 3, 4, 5], 30),
    ([], 0),
    ([2, 2, 2, 2], 8),
    ([1, 3, 3, 1, 10], 140),
    ([-11, 3, 3, 1, 10], 20),
]


@pytest.mark.parametrize(
    "numbers, expected", data
)
def test_even_last(numbers, expected):
    assert even_last(numbers) == expected
