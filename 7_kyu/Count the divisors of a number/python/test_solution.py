import pytest

from solution import divisors

data = [
    (4, 3),
    (5, 2),
    (12, 6),
    (30, 8),
    (4096, 13),
]


@pytest.mark.parametrize("n, result", data)
def test_divisors(n, result):
    assert divisors(n) == result
