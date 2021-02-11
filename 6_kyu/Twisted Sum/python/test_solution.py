import pytest

from solution import compute_sum


data = [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (10, 46),
    (12, 51),
]


@pytest.mark.parametrize("n, result", data)
def test_compute_sum(n, result):
    assert compute_sum(n) == result
