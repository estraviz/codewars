import pytest

from solution import prime_factors


tests = [
    (1, []),
    (3, [3]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (12, [2, 2, 3]),
    (11020332, [2, 2, 3, 918361]),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_prime_factors(n, expected):
    assert prime_factors(n) == expected
