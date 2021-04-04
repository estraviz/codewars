import pytest

from solution import generate_range


data = [
    (1, 10, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (-10, 1, 1, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]),
    (1, 15, 20, [1]),
    (1, 7, 2, [1, 3, 5]),
    (0, 20, 3, [0, 3, 6, 9, 12, 15, 18]),
]


@pytest.mark.parametrize(
    "min, max, step, result", data
)
def test_generate_range(min, max, step, result):
    assert generate_range(min, max, step) == result
