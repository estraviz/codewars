import pytest

from solution import no_odds


data = [
    ([0, 1], [0]),
    ([0, 1, 2, 3], [0, 2]),
    ([1, 3, 5, 7, 9], []),
    ([0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10]),
    ([-1, -3, -5, -7, -9], []),
    ([2, 4, 8, 6, 0], [2, 4, 8, 6, 0]),
    ([], []),
]


@pytest.mark.parametrize("values, result", data)
def test_no_odds(values, result):
    assert no_odds(values) == result
