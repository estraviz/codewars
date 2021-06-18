import pytest

from solution import nbr_of_laps


tests = [
    (5, 3, (3, 5)),
    (4, 6, (3, 2)),
    (5, 5, (1, 1)),
]


@pytest.mark.parametrize(
    "x, y, expected", tests
)
def test_nbr_of_laps(x, y, expected):
    assert nbr_of_laps(x, y) == expected
