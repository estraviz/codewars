import pytest

from solution import calc

data = [
    ('abcdef', 6),
    ('ifkhchlhfd', 6),
    ('aaaaaddddr', 30),
    ('jfmgklf8hglbe', 6),
    ('jaam', 12),
    ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 96),
]

@pytest.mark.parametrize(
    "x, result", data
)
def test_calc(x, result):
    assert calc(x) == result
