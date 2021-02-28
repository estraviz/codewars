import pytest

from solution import flip


data = [
    ('R', [4, 5, 6, 7, 1], [1, 4, 5, 6, 7]),
    ('L', [3, 0, 9, 8, 1, 2], [9, 8, 3, 2, 1, 0]),
    ('L', [0, 0, 12, 0, 1], [12, 1, 0, 0, 0]),
    ('R', [13, 2, 4, 7, 93], [2, 4, 7, 13, 93]),
    ('R', [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize(
    "d, a, result", data
)
def test_flip(d, a, result):
    assert flip(d, a) == result
