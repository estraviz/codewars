import pytest

from solution import perfect_roots


data = [
    (256, True),
    (1000, False),
    (6561, True),
]


@pytest.mark.parametrize(
    "n, result", data
)
def test_perfect_roots(n, result):
    assert perfect_roots(n) == result
