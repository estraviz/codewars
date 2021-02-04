import pytest

from solution import convert_bits

data = [
    (31, 14, 2),
    (7, 17, 3),
    (31, 0, 5),
    (0, 0, 0),
    (127681, 127681, 0),
    (312312312, 5645657, 13),
    (43, 2009989843, 17),
]


@pytest.mark.parametrize("a, b, result", data)
def test_convert_bits(a, b, result):
    assert convert_bits(a, b) == result
