import pytest

from solution import digitize


data = [
    (123, [1, 2, 3]),
    (1, [1]),
    (0, [0]),
    (1230, [1, 2, 3, 0]),
    (8675309, [8, 6, 7, 5, 3, 0, 9]),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_digitize(n, expected):
    assert digitize(n) == expected
