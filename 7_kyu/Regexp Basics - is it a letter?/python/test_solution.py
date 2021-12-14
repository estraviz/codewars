import pytest

from solution import is_letter


tests = [
    ("", False),
    ("a", True),
    ("X", True),
    ("7", False),
    ("_", False),
    ("ab", False),
    ("a\n", False),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_is_letter(s, expected):
    assert is_letter(s) == expected
