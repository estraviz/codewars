import pytest

from solution import over_the_road


tests = [
    (1, 3, 6),
    (3, 3, 4),
    (2, 3, 5),
    (3, 5, 8),
    (7, 11, 16),
    (23633656673, 310027696726, 596421736780),
    (10, 22, 35),
    (20, 3400, 6781),
    (9, 26, 44),
    (20, 10, 1),
]


@pytest.mark.parametrize(
    "address, n, expected", tests
)
def test_over_the_road(address, n, expected):
    assert over_the_road(address, n) == expected
