import pytest

from solution import number_joy


tests = [
    (1997, False),
    (1998, False),
    (1729, True),
    (18, False),
    (1, True),
    (81, True),
    (1458, True),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_number_joy(n, expected):
    assert number_joy(n) == expected
