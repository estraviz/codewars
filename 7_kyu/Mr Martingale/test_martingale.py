from solution import martingale
import pytest


@pytest.mark.parametrize(
    "bankroll, rounds, output",
    [[500, [], 500],
     [1000, [1, 1, 0, 0, 1], 1300],
     [0, [0, 0, 0, 0, 1, 0, 0], -200],
     [5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0], 5600],
     [-500, [1, 1, 0, 1, 0, 1, 0], -200]]
)
def test_martingale(bankroll, rounds, output):
    assert martingale(bankroll, rounds) == output
