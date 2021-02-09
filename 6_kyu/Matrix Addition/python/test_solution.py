import pytest

from solution import matrix_addition


data = [
    ([[1, 2], [1, 2]], [[2, 3], [2, 3]], [[3, 5], [3, 5]]),
    ([[1]], [[2]], [[3]]),
    (
        [[1, 2, 3], [3, 2, 1], [1, 1, 1]],
        [[2, 2, 1], [3, 2, 3], [1, 1, 3]],
        [[3, 4, 4], [6, 4, 4], [2, 2, 4]],
    ),
]


@pytest.mark.parametrize("a, b, result", data)
def test_matrix_addition(a, b, result):
    assert matrix_addition(a, b) == result
