import pytest

from solution import check_alive


data = [
    (5, True),
    (0, False),
    (-5, False),
]

@pytest.mark.parametrize(
    "health, result", data
)
def test_check_alive(health, result):
    assert check_alive(health) == result
