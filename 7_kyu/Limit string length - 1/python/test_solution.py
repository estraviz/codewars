import pytest

from solution import solution

data = [
    ("Testing String", 3, "Tes..."),
    ("Testing String", 8, "Testing ..."),
    ("Test", 10, "Test"),
    ("Test", 4, "Test"),
]


@pytest.mark.parametrize("st, limit, result", data)
def test_solution(st, limit, result):
    assert solution(st, limit) == result
