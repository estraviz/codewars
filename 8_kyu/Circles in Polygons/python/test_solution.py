import pytest

from solution import circle_diameter


tests = [
    ((4, 5), 5.000),
    ((8, 9), 21.728),
    ((3, 4), 2.309)
]


@pytest.mark.parametrize(
    "data, expected", tests
)
def test_circle_diameter(data, expected):
    sides, side_length = data
    assert circle_diameter(sides, side_length) == expected
