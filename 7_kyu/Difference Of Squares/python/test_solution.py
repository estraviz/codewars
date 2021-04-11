import pytest

from solution import difference_of_squares


data = [
    (5, 170),
    (10, 2640),
    (100, 25164150),
]


@pytest.mark.parametrize(
    "n, result", data
)
def test_difference_of_square(n, result):
    assert difference_of_squares(n) == result
