import pytest

from solution import reverse_number


data = [
    (123, 321),
    (-123, -321),
    (1000, 1),
    (4321234, 4321234),
    (5, 5),
    (0, 0),
    (98989898, 89898989),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_reverse_number(n, expected):
    assert reverse_number(n) == expected
