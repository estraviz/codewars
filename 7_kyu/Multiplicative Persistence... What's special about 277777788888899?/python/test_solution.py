import pytest

from solution import per


assorted_tests = [
    (1234567890, [0]),
    (123456789, [362880, 0]),
    (12345678, [40320, 0]),
    (1234567, [5040, 0]),
    (123456, [720, 0]),
    (12345, [120, 0]),
    (2379, [378, 168, 48, 32, 6]),
    (777, [343, 36, 18, 8]),
    (25, [10, 0]),
]


@pytest.mark.parametrize(
    "n, expected", assorted_tests
)
def test_multiplicative_persistence_for_assorted_tests(n, expected):
    assert per(n) == expected


large_tests = [
    (277777788888899,
     [4996238671872, 438939648, 4478976, 338688, 27648, 2688, 768, 336, 54, 20, 0]),
    (3778888999,
     [438939648, 4478976, 338688, 27648, 2688, 768, 336, 54, 20, 0]),
]


@pytest.mark.parametrize(
    "n, expected", large_tests
)
def test_multiplicative_persistence_for_large_tests(n, expected):
    assert per(n) == expected
