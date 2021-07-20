import pytest

from solution import encode
from solution import decode


tests_encode = [
    ('hello', 'h2ll4'),
    ('How are you today?', 'H4w 1r2 y45 t4d1y?'),
    ('This is an encoding test.', 'Th3s 3s 1n 2nc4d3ng t2st.'),
]


@pytest.mark.parametrize(
    "st, expected", tests_encode
)
def test_encoding(st, expected):
    assert encode(st) == expected


tests_decode = [
    ('h2ll4', 'hello'),
]


@pytest.mark.parametrize(
    "st, expected", tests_decode
)
def test_decoding(st, expected):
    assert decode(st) == expected
