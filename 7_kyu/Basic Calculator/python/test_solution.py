import pytest

from solution import calculate


example_data = [
    (3.2, "+", 8, 11.2),
    (3.2, "-", 8, -4.8),
    (3.2, "/", 8, 0.4),
    (3.2, "*", 8, 25.6),
    (-3, "+", 0, -3),
    (-3, "-", 0, -3),
    (-2, "/", -2, 1),
    (-3, "*", 0, 0),
]


@pytest.mark.parametrize(
    "num1, operation, num2, expected", example_data
)
def test_should_validate_simple_test_cases(num1, operation, num2, expected):
    assert calculate(num1, operation, num2) == expected


edge_case_data = [
    (-3, "/", 0, None, "-3 / 0 = None"),
    (-3, "w", 0, None, "-3 w 0 = None"),
    (-3, "w", 1, None, "-3 w 1 = None"),
]


@pytest.mark.parametrize(
    "num1, operation, num2, expected", example_data
)
def test_should_validate_edge_test_cases(num1, operation, num2, expected):
    assert calculate(num1, operation, num2) == expected
