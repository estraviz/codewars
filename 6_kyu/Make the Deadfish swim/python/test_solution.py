import pytest

from solution import parse


data = [
    ("ooo", [0, 0, 0]),
    ("ioioio", [1, 2, 3]),
    ("idoiido", [0, 1]),
    ("isoisoiso", [1, 4, 25]),
    ("codewars", [0]),
]


@pytest.mark.parametrize(
    "data, expected", data
)
def test_should_make_deadfish_swim(data,expected):
    assert parse(data) == expected
