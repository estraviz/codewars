import pytest

from solution import combat

data = [
    (100, 5, 95),
    (92, 8, 84),
    (20, 30, 0),
    (0, 100, 0),
    (50, 0, 50),
]

@pytest.mark.parametrize(
    "health, damage, result", data
)
def test_combat(health, damage, result):
    assert combat(health, damage) == result
