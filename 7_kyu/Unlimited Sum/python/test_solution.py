import pytest

from solution import sum

data = [
    ((1, 2, 3), 6),
    ((1, "2", 3), 4),
    ((1,), 1),
    ((1, 2, 3), 6),
    ((-1, 2, -3), -2),
    (("a", 1), 1),
    (("a", [], {}, str, 1, 3), 4),
]


@pytest.mark.parametrize("args, result", data)
def test_sum(args, result):
    assert sum(*args) == result
