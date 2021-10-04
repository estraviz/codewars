import pytest

from solution import is_alt


tests = [
    ("amazon", True),
    ("apple", False),
    ("banana", True),
    ("orange", False),
    ("helipad", True),
    ("yay", True),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_is_alt(s, expected):
    assert is_alt(s) == expected
