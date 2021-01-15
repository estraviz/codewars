from _pytest.config import exceptions
import pytest

from solution import factorial


data = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
    (11, 39916800),
    (12, 479001600),
]


@pytest.mark.parametrize("n, result", data)
def test_passes(n, result):
    assert factorial(n) == result


not_valid_data = [
    (-1, ValueError),
    (-100, ValueError),
    (22, ValueError),
]


@pytest.mark.parametrize("n, result", not_valid_data)
def test_raises(n, result):
    with pytest.raises(ValueError):
        assert factorial(n)
