import pytest

from solution import generate_shape


data = [
    (3, '+++\n+++\n+++'),
    (8, '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_should_generate_squared_shapes(n, expected):
    assert generate_shape(n) == expected
