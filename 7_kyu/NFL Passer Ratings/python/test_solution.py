import pytest

from solution import passer_rating


data = [
    (432, 3554, 291, 28, 2, 112.2),
    (5, 76, 4, 1, 0, 158.3),
    (48, 192, 19, 2, 3, 39.6),
    (1, 2, 1, 1, 0, 118.8),
    (34, 172, 20, 1, 1, 69.7),
    (10, 17, 2, 0, 1, 0.0),

]


@pytest.mark.parametrize(
    "att, yds, comp, td, ints, result", data
)
def test_passer_rating(att, yds, comp, td, ints, result):
    assert passer_rating(att, yds, comp, td, ints) == result
