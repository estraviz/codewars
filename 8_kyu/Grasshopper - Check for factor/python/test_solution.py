import pytest

from solution import check_for_factor

data = [
    (10, 2, True),
    (63, 7, True),
    (2450, 5, True),
    (24612, 3, True),
    (9, 2, False),
    (653, 7, False),
    (2453, 5, False),
    (24617, 3, False),
]

@pytest.mark.parametrize(
    "base, factor, expected", data
)
def test_check_for_factor(base, factor, expected):
    assert check_for_factor(base, factor) == expected
