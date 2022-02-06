import pytest

from solution import grid_map


@pytest.fixture
def num_grid():
    return [[1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 2, 4]]


@pytest.fixture
def char_grid():
    return [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]


def test_addition(num_grid):
    expected = [[2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 3, 5]]
    assert grid_map(num_grid, lambda x: x + 1) == expected


def test_multiplication(num_grid):
    expected = [[2, 4, 6, 8], [10, 12, 14, 16, 18], [0, 4, 8]]
    assert grid_map(num_grid, lambda x: x * 2) == expected


def test_power(num_grid):
    expected = [[1, 4, 9, 16], [25, 36, 49, 64, 81], [0, 4, 16]]
    assert grid_map(num_grid, lambda x: x ** 2) == expected


def test_upper(char_grid):
    expected = [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]
    assert grid_map(char_grid, lambda x: x.upper()) == expected


def test_lower(char_grid):
    expected = [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]
    assert grid_map(char_grid, lambda x: x.lower()) == expected
