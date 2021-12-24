import pytest

from solution import bits_battle


tests = [
    ([5, 3, 14], 'odds win'),
    ([3, 8, 22, 15, 78], 'evens win'),
    ([], 'tie'),
    ([1, 13, 16], 'tie'),
]


@pytest.mark.parametrize(
    "numbers, expected", tests
)
def test_bits_battle(numbers, expected):
    assert bits_battle(numbers) == expected
