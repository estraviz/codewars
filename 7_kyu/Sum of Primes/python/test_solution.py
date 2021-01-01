import pytest

from solution import sum_primes


data = [
    (4, 20, 72),
    (20, 4, 0),
    (2, 7, 17),
    (1, 30, 129),
]


@pytest.mark.parametrize("lower, upper, result", data)
def test_sum_primes(lower, upper, result):
    assert sum_primes(lower, upper) == result
