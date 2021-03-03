import pytest

from solution import logical_calc


data = [
    ([True, False], "AND", False),
    ([True, False], "OR", True),
    ([True, False], "XOR", True),
    ([True, True, False], "AND", False),
    ([True, True, False], "OR", True),
    ([True, True, False], "XOR", False),
    ([True, True, True, False], "AND", False),
    ([True, True, True, False], "OR", True),
    ([True, True, True, False], "XOR", True),
    ([True, True, False, False], "AND", False),
    ([True, True, False, False], "OR", True),
    ([True, True, False, False], "XOR", False),
    ([True, False, False, False], "AND", False),
    ([True, False, False, False], "OR", True),
    ([True, False, False, False], "XOR", True),
    ([True, True], "AND", True),
    ([True, True], "OR", True),
    ([True, True], "XOR", False),
    ([False, False], "AND", False),
    ([False, False], "OR", False),
    ([False, False], "XOR", False),
    ([False], "AND", False),
    ([False], "OR", False),
    ([False], "XOR", False),
    ([True], "AND", True),
    ([True], "OR", True),
    ([True], "XOR", True),
]


@pytest.mark.parametrize(
    "array, op, result", data
)
def test_logical_cal(array, op, result):
    assert logical_calc(array, op) == result
