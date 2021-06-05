import pytest

from solution import get_missing_element


data = [
    ([0, 5, 1, 3, 2, 9, 7, 6, 4], 8),
    ([9, 2, 4, 5, 7, 0, 8, 6, 1], 3),
]


@pytest.mark.parametrize(
    "seq, expected", data
)
def test_get_missing_element(seq, expected):
    assert get_missing_element(seq) == expected
