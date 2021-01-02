import pytest

from solution import double_every_other


data = [
    ([1, 2, 3, 4, 5], [1, 4, 3, 8, 5]),
    ([1, 19, 6, 2, 12, -3], [1, 38, 6, 4, 12, -6]),
    ([-1000, 1653, 210, 0, 1], [-1000, 3306, 210, 0, 1]),
]


@pytest.mark.parametrize("lst, result", data)
def test_double_every_other(lst, result):
    assert double_every_other(lst) == result
