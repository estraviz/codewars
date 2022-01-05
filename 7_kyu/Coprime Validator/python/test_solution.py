import pytest

from solution import are_coprime


basic_tests = [
    (20, 27, True),
    (12, 39, False),
    (17, 34, False),
    (34, 17, False),
    (35, 10, False),
    (64, 27, True),
]


@pytest.mark.parametrize(
    "n, m, expected", basic_tests
)
def test_are_coprime(n, m, expected):
    assert are_coprime(n, m) == expected
