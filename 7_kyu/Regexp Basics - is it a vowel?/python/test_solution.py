import pytest

from solution import is_vowel


tests = [
    ("", False),
    ("a", True),
    ("E", True),
    ("ou", False),
    ("z", False),
    ("lol", False),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_is_vowel(s, expected):
    assert is_vowel(s) == expected
