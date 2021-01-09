import pytest

from solution import cube_sum


data = [
    (5, 0, 225),
    (2, 3, 27),
    (999, 1000, 1000000000),
    (100, 101, 1030301),
    (11, 15, 10044),
    (6, 6, 0),
]


@pytest.mark.parametrize("n, m, result", data)
def test_cube_sum(n, m, result):
    assert cube_sum(n, m) == result
