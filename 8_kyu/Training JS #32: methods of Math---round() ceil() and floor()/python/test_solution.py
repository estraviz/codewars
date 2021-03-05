import pytest

from solution import round_it


data = [
    (3.45, 4),
    (34.5, 34),
    (34.56, 35),
]


@pytest.mark.parametrize(
    "n, result", data
)
def test_round_it(n, result):
    assert round_it(n) == result
