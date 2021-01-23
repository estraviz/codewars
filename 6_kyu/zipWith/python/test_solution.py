import pytest

from solution import zip_with


data = [
    (lambda a, b: a + b, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1], [6, 6, 6, 6, 6, 6]),
    (lambda a, b: a + b, [0, 1, 2, 3, 4], [6, 5, 4, 3, 2, 1], [6, 6, 6, 6, 6]),
    (lambda a, b: a + b, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2], [6, 6, 6, 6, 6]),
    (lambda a, b: a ** b, [10, 10, 10, 10], [0, 1, 2, 3], [1, 10, 100, 1000]),
    (
        lambda a, b: max([a, b]),
        [1, 4, 7, 1, 4, 7],
        [4, 7, 1, 4, 7, 1],
        [4, 7, 7, 4, 7, 7],
    ),
    (lambda a, b: a + b, [0, 1, 2, 3], [0, 1, 2, 3], [0, 2, 4, 6]),
    (lambda a, b: a + b, [0, 1, 2, 3], [0, 1, 2, 3], [0, 2, 4, 6]),
    (
        lambda a, b: a ** b,
        [10, 10, 10, 10, 10, 10, 10],
        [0, 1, 2, 3, 4, 5, 6],
        [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6],
    ),
    (lambda a, b: a - b, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1], [-6, -4, -2, 0, 2, 4]),
    (
        lambda a, b: a * b,
        ["a", "b", "c", "d", "e", "f"],
        [6, 5, 4, 3, 2, 1],
        ["aaaaaa", "bbbbb", "cccc", "ddd", "ee", "f"],
    ),
]


@pytest.mark.parametrize("fn, a1, a2, result", data)
def test_zip_with(fn, a1, a2, result):
    assert zip_with(fn, a1, a2) == result
