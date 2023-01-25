import pytest

from solution import yahtzee_upper

tests = [
    ([2, 3, 5, 5, 6], 10),
    ([1, 1, 1, 1, 3], 4),
    ([1, 1, 1, 3, 3], 6),
    ([1, 2, 3, 4, 5], 5),
    ([6, 6, 6, 6, 6], 30),
    ([15, 9, 9, 8, 9], 27),
    (
        [
            1654, 1654, 5099, 3086, 1654, 5099, 2274, 1654, 1654, 1654, 1654,
            1654, 3086, 4868, 1654, 4868, 1654, 3086, 4868, 3086
        ], 16540
    )
]


@pytest.mark.parametrize(
    "dice, expected", tests
)
def test_yahtzee_upper(dice, expected):
    assert yahtzee_upper(dice) == expected
