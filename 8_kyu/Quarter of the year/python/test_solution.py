import pytest

from solution import quarter_of


data = [
    (3, 1),
    (8, 3),
    (11, 4),
]


@pytest.mark.parametrize(
    "month, result", data
)
def test_quarter_of(month, result):
    assert quarter_of(month) == result
