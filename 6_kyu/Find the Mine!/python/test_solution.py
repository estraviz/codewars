import pytest

from solution import mineLocation


tests = [
    ([[1, 0], [0, 0]], [0, 0]),
    ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0]),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [2, 2]),
]


@pytest.mark.parametrize(
    "field, expected", tests
)
def test_mineLocation(field, expected):
    assert mineLocation(field) == expected
