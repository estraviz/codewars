import pytest

from solution import sum_triangular_numbers


data = [
    (6, 56),
    (34, 7140),
    (-291, 0),
    (943, 140205240),
    (-971, 0),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_sum_triangular_numbers(n, expected):
    assert sum_triangular_numbers(n) == expected
