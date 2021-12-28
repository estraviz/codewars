import pytest

from solution import remainder


tests = [
    (17, 5, 2),
    (13, 72, remainder(72, 13)),
    (1, 0, None),
    (0, 0, None),
    (0, 1, None),
    (-1, 0, 0),
    (0, -1, 0),
    (-13, -13, 0),
    (-60, 340, -20),
    (60, -40, -20),
]


@pytest.mark.parametrize(
    "a, b, expected", tests
)
def test_remainder(a, b, expected):
    assert remainder(a, b) == expected
