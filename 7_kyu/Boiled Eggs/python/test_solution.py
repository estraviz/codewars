import pytest

from solution import cooking_time


data = [
    (0, 0),
    (1, 5),
    (5, 5),
    (8, 5),
    (9, 10),
    (10, 10),
    (16, 10),
    (20, 15),
    (100, 65),
]


@pytest.mark.parametrize(
    "eggs, expected", data
)
def test_eggs(eggs, expected):
    assert cooking_time(eggs) == expected
