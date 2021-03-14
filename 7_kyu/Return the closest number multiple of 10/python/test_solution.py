import pytest

from solution import closest_multiple_10


data = [
    (54, 50),
    (55, 60),
]


@pytest.mark.parametrize(
    "i, result", data
)
def test_closest_multiple_10(i, result):
    assert closest_multiple_10(i) == result
