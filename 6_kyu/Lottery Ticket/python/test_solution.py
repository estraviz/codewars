import pytest

from solution import bingo


tests = [
    ([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2, 'Loser!'),
    ([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1, 'Winner!'),
    ([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3, 'Loser!'),
]


@pytest.mark.parametrize(
    "ticket, win, expected", tests
)
def test_bingo(ticket, win, expected):
    assert bingo(ticket, win) == expected
