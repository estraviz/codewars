from math import isclose
import pytest

from solution import variance


data = [
    ([-10, 0, 10, 20, 30], 200),
    ([8, 9, 10, 11, 12], 2),
    ([1.5, 2.5, 4, 2, 1, 1], 1.0833333333333333),
    ([10, 20, 50, 0, -100], 2584),
    ([1, 2], 0.25),
    ([-1, -10, -500], 54353.55555555555),
    ([800], 0),
]


@pytest.mark.parametrize("numbers, result", data)
def test_variance(numbers, result):
    assert isclose(variance(numbers), result, rel_tol=1e-09)
    assert variance(numbers) == pytest.approx(result, rel=1e-09)  # equivalent
