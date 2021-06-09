import pytest

from solution import halving_sum


data = [
    (25, 47),
    (127, 247),
    (38, 73),
    (1, 1),
    (320, 638),
    (13, 23),
    (15, 26),
    (47, 89),
    (101, 198),
    (257, 512),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_halving_sum(n, expected):
    assert halving_sum(n) == expected
