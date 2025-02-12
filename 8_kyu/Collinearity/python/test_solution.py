import pytest

from solution import collinearity

vectors_in_one_direction = [
    (1, 1, 1, 1, True),
    (1, 2, 2, 4, True),
]

@pytest.mark.parametrize(
    "x1, y1, x2, y2, result", vectors_in_one_direction
)
def test_vectors_in_one_direction(x1, y1, x2, y2, result):
    assert collinearity(x1, y1, x2, y2) == result


vectors_in_opposite_direction = [
    (1, 1, 6, 1, False),
    (1, 2, -1, -2, True),
    (1, 2, 1, -2, False),
]

@pytest.mark.parametrize(
    "x1, y1, x2, y2, result", vectors_in_opposite_direction
)
def test_vectors_in_opposite_direction(x1, y1, x2, y2, result):
    assert collinearity(x1, y1, x2, y2) == result

vectors_contain_zero = [
    (4, 0, 11, 0, True),
    (0, 1, 6, 0, False),
    (4, 4, 0, 4, False),
]

@pytest.mark.parametrize(
    "x1, y1, x2, y2, result", vectors_contain_zero
)
def test_vectors_contain_zero(x1, y1, x2, y2, result):
    assert collinearity(x1, y1, x2, y2) == result

vectors_with_coordinates_x_equals_0_and_y_equals_0 = [
    (0, 0, 0, 0, True),
    (0, 0, 1, 0, True),
    (5, 7, 0, 0, True),
]

@pytest.mark.parametrize(
    "x1, y1, x2, y2, result", vectors_with_coordinates_x_equals_0_and_y_equals_0
)
def test_vectors_with_coordinates_x_equals_0_and_y_equals_0(x1, y1, x2, y2, result):
    assert collinearity(x1, y1, x2, y2) == result
