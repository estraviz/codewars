import pytest

from solution import bumps


tests = [
    ("n", "Woohoo!"),
    ("_nnnnnnn_n__n______nn__nn_nnn", "Car Dead"),
    ("______n___n_", "Woohoo!"),
    ("nnnnnnnnnnnnnnnnnnnnn", "Car Dead"),
]


@pytest.mark.parametrize(
    "road, expected", tests
)
def test_bumps(road, expected):
    assert bumps(road) == expected
