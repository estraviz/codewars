import pytest

from solution import monkey_count

data = [
    (5, [1, 2, 3, 4, 5]),
    (1, [1]),
    (0, []),
    (12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
]

@pytest.mark.parametrize(
    "n, result", data
)
def test_monkey_count(n, result):
    assert monkey_count(n) == result
