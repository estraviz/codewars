import pytest

from solution import sqInRect

data = [
    (5, 5, None),
    (5, 3, [3, 2, 1, 1]),
    (3, 5, [3, 2, 1, 1]),
    (20, 14, [14, 6, 6, 2, 2, 2]),
    (14, 20, [14, 6, 6, 2, 2, 2]),
    (240, 32, [32, 32, 32, 32, 32, 32, 32, 16, 16]),
    (6250, 250, [250] * 25),
    (625, 230, [230, 230, 165, 65, 65, 35, 30, 5, 5, 5, 5, 5, 5]),
    (731, 230, [230, 230, 230, 41, 41, 41, 41, 41, 25, 16, 9, 7, 2, 2, 2, 1, 1]),
    (37, 14, [14, 14, 9, 5, 4, 1, 1, 1, 1]),
]


@pytest.mark.parametrize("lng, wdth, result", data)
def test_sqInRect(lng, wdth, result):
    assert sqInRect(lng, wdth) == result
