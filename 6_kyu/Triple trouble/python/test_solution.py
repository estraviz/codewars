import pytest

from solution import triple_double


data = [
    (451999277, 41177722899, 1),
    (1222345, 12345, 0),
    (12345, 12345, 0),
    (666789, 12345667, 1),
    (10560002, 100, 1),
    (1112, 122, 0),
]


@pytest.mark.parametrize(
    "num1, num2, result", data
)
def test_triple_double(num1, num2, result):
    assert triple_double(num1, num2) == result
