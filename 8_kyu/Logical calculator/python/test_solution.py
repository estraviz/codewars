import pytest

from solution import logical_calc


data = [
    ([True, False], "AND", False),
    ([True, False], "OR", True),
    ([True, False], "XOR", True),
    ([True, True, False], "AND", False),
    ([True, True, False], "OR", True),
    ([True, True, False], "XOR", False),
]


@pytest.mark.parametrize(
    "array, op, result", data
)
def test_logical_cal(array, op, result):
    assert logical_calc(array, op) == result
