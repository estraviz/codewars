import pytest

from solution import max_multiple


data = [
    (2, 7, 6),
    (3, 10, 9),
    (7, 17, 14),
    (10, 50, 50),
    (37, 200, 185),
    (7, 100, 98),
]


@pytest.mark.parametrize(
    "divisor, bound, result", data
)
def test_max_multiple(divisor, bound, result):
    assert max_multiple(divisor, bound) == result
