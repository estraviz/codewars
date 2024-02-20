import pytest
from twice_as_old import twice_as_old

data = [
    (36, 7, 22),
    (55, 30, 5),
    (42, 21, 0),
    (22, 1, 20),
    (29, 0, 29),
]


@pytest.mark.parametrize('dad_years_old, son_years_old, result', data)
def test_twice_as_old(dad_years_old, son_years_old, result):
    assert twice_as_old(dad_years_old, son_years_old) == result
