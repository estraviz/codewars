import pytest

from solution import cake


tests = [
    (900, 'abcdef', 'That was close!'),
    (56, 'ifkhchlhfd', 'Fire!'),
    (256, 'aaaaaddddr', 'Fire!'),
    (333, 'jfmgklfhglbe', 'Fire!'),
    (12, 'jaam', 'Fire!'),
    (808, "alfbpmmpz", "Fire!"),
    (660, "zyxsqwh", "Fire!"),
    (651, "hmgoltyy", "Fire!"),
    (349, "nxls", "Fire!"),
    (958, "hovzfsxbmwu", "Fire!"),
    (301, "doda", "Fire!"),
    (383, "zwwl", "Fire!"),
    (871, "gnlyvknjga", "That was close!"),
    (583, "slhacx", "That was close!"),
    (0, "jpipe", "That was close!"),
]


@pytest.mark.parametrize(
    "candles, debris, expected", tests
)
def test_cake(candles, debris, expected):
    assert cake(candles, debris) == expected
