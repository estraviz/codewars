import pytest

from solution import plural

data = [
    (0, True),
    (1, False),
    (100, True),
]


@pytest.mark.parametrize("n, expected", data)
def test_solution(n, expected):
    assert plural(n) is expected
