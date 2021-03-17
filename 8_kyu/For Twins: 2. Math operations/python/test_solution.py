import pytest

from solution import ice_brick_volume


data_basic = [
    (1, 10, 2, 16),
    (5, 30, 7, 1150),
]


@pytest.mark.parametrize(
    "radius, bottle_length, rim_length, result", data_basic
)
def test_ice_brick_volume_simple(radius, bottle_length, rim_length, result):
    assert ice_brick_volume(radius, bottle_length, rim_length) == result


data_advanced = [
    (1, 3, 2, 2),
    (4, 14, 2, 384),
    (8, 100, 96, 512),
    (13, 19, 3, 5408),
    (2, 9, 0, 72),
    (32, 7, 3, 8192),
    (2, 13, 2, 88),
    (1, 2, 0, 4),
    (11, 17, 3, 3388),
    (2, 8, 0, 64),
]


@pytest.mark.parametrize(
    "radius, bottle_length, rim_length, result", data_advanced
)
def test_ice_brick_volume_advanced(radius, bottle_length, rim_length, result):
    assert ice_brick_volume(radius, bottle_length, rim_length) == result
