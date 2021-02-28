import pytest

from solution import odds


data = [
    ([], []),
    ([2, 4, 6], []),
    ([1, 3, 5], [1, 3, 5]),
    ([1, 2, 3, 4, 5, 6], [1, 3, 5]),
]

@pytest.mark.parametrize(
    "x, result", data
)
def test_odds(x, result):
    assert odds(x) == result
