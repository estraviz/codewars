import pytest

from solution import find_smallest

data = [
    ([5, 4, 3, 2, 1], "value", 1),
    ([5, 4, 3, 2, 1], "index", 4),
    ([8, 0, 9], "index", 1),
    ([8, 0, 9], "value", 0),
    ([1, 1, 0, 0, 1, 1], "value", 0),
    ([1, 1, 0, 0, 1, 1], "index", 2),
]


@pytest.mark.parametrize("numbers, to_return, result", data)
def test_find_smallest(numbers, to_return, result):
    assert find_smallest(numbers, to_return) == result
