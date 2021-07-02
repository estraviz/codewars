import pytest

from solution import make_2d_list


tests = [
    (1, 2, 3, [[1, 2, 3], [4, 5, 6]]),
    (2, 3, 4, [[2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]]),
    (5, 6, 1, [[5], [6], [7], [8], [9], [10]]),
    (7, 1, 1, [[7]]),
    (0, 1, 0, [[]]),
    (-20, 2, 2, [[-20, -19], [-18, -17]]),
    (10**10, 2, 2, [[10000000000, 10000000001], [10000000002, 10000000003]]),
]


@pytest.mark.parametrize(
    "head, row, col, expected", tests
)
def test_make_2d_list(head, row, col, expected):
    assert make_2d_list(head, row, col) == expected
