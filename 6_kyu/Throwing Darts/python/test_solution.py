import pytest

from solution import score_throws


tests = [
    ([1, 5, 11], 15),
    ([15, 20, 30, 31, 32, 44, 100], 0),
    ([1, 2, 3, 4], 140),
    ([], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 65),
    ([0, 5, 10, 10.5, 4.5], 30),
    ([1], 110),
    ([21, 10, 10], 10),
    ([5, 5, 5, 5], 20),
    ([4.9, 5.1], 15),
]


@pytest.mark.parametrize(
    "radii, expected", tests
)
def test_radii(radii, expected):
    assert score_throws(radii) == expected
