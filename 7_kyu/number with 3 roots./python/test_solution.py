import pytest

from solution import perfect_roots


data = [
    (256, True),
    (1000, False),
    (6561, True),
    (12534, False),
    (3455, False),
    (65536, True),
    (390625, True),
    (1679616, True),
    (6534561, False),
    (253456, False),
    (5764801, True),
    (100000000, True),
]


@pytest.mark.parametrize(
    "n, result", data
)
def test_perfect_roots(n, result):
    assert perfect_roots(n) == result
