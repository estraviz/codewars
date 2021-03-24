import pytest

from solution import mygcd


data = [
    (30, 12, 6),
    (8, 9, 1),
    (1, 1, 1),
    (10927782, 6902514, 846),
    (1590771464, 1590771620, 4),
    (1, 3, 1),
    (60, 12, 12),
    (2672, 5678, 334),
]


@pytest.mark.parametrize(
    "x, y, result", data
)
def test_mygcd(x, y, result):
    assert mygcd(x, y) == result
