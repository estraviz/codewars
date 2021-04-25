import pytest

from solution import f


data = [
    (1, 1),
    (100, 5050),
    (300, 45150),
    (303, 46056),
    (50000, 1250025000),
    ('n', None),
    (3.14, None),
    (0, None),
    (-10, None),

]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_f(n, expected):
    assert f(n) == expected
