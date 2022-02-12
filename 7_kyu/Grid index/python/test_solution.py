import pytest

from solution import grid_index


basic_tests = [
    (
        [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']],
        [1, 2, 3, 4, 5, 6, 7, 8, 9], 'myexample'
    ),
    (
        [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']],
        [1, 5, 6], 'mam'
    ),
    (
        [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']],
        [1, 3, 7, 8], 'mepl'
    ),
    (
        [
            ['h', 'e', 'l', 'l'],
            ['o', 'c', 'o', 'd'],
            ['e', 'w', 'a', 'r'],
            ['r', 'i', 'o', 'r']
        ],
        [5, 7, 9, 3, 6, 6, 8, 8, 16, 13], 'ooelccddrr'
    ),
]


@pytest.mark.parametrize(
    "grid, indexes, expected", basic_tests
)
def test_grid_index(grid, indexes, expected):
    assert grid_index(grid, indexes) == expected
