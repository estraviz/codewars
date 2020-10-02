from solution import say_me_operations
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [
        ("1 2 3 5 8", "addition, addition, addition"),
        ("9 4 5 20 25", "subtraction, multiplication, addition"),
        ("10 2 5 -3 -15 12", "division, subtraction, multiplication, subtraction"),
        ("2 2 4", "addition"),
        pytest.param("3 3 6", "subtraction", marks=pytest.mark.xfail),
        pytest.param("1 0 5", "division", marks=pytest.mark.xfail),
        pytest.param("5 2 2.5", "division", marks=pytest.mark.xfail),
    ],
)
def test_say_me_operations(test_input, expected):
    assert say_me_operations(test_input) == expected
