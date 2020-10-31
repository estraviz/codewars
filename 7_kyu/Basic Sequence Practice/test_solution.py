import pytest
from solution import sum_of_n


@pytest.mark.parametrize(
    "n, seq",
    [
        [3, [0, 1, 3, 6]],
        [1, [0, 1]],
        [0, [0]],
        [-4, [0, -1, -3, -6, -10]],
        [10, [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]]
    ]
)
def test_sum_of_n(n, seq):
    assert sum_of_n(n) == seq
