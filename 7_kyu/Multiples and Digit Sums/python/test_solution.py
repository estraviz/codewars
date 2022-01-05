import pytest

from solution import procedure


tests = [
    (25, 25),
    (30, 18),
    (12, 72),
]


@pytest.mark.parametrize(
    "i, expected", tests
)
def test_procedure(i, expected):
    assert procedure(i) == expected

