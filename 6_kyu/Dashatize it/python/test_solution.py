import pytest

from solution import dashatize


data = [
    (274, "2-7-4"),
    (5311, "5-3-1-1"),
    (86320, "86-3-20"),
    (974302, "9-7-4-3-02"),
    (None, "None"),
    (0, "0"),
    (-1, "1"),
    (-28369, "28-3-6-9"),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_dashatize(n, expected):
    assert dashatize(n) == expected
