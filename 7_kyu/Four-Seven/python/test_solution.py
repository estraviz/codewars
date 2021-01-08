import pytest

from solution import solution


data = [(7, 4), (4, 7)]


@pytest.mark.parametrize("n, result", data)
def test_solution(n, result):
    assert solution(n) == result
