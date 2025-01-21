import pytest

from solution import simple_multiplication

data = [
    (2, 16),
    (1, 9),
    (8, 64),
    (4, 32),
    (3, 27),
    (9, 81),
    (5, 45),
    (6, 48),
    (7, 63),
    (10, 80),
]

@pytest.mark.parametrize(
    "number, result", data
)
def test_simple_multiplication(number, result):
    assert simple_multiplication(number) == result
