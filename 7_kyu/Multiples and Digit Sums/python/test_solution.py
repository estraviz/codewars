import pytest

from solution import procedure


tests = [
    (25, 25),
    (30, 18),
    (12, 72),
    (49, 30),
    (17, 48),
    (10, 46),
]


@pytest.mark.parametrize(
    "i, expected", tests
)
def test_procedure(i, expected):
    assert procedure(i) == expected

