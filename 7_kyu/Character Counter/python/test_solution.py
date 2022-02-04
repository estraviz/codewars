import pytest

from solution import validate_word


tests = [
    ("abcabc", True),
    ("Abcabc", True),
    ("AbcabcC", False),
    ("AbcCBa", True),
    ("pippi", False),
    ("?!?!?!", True),
    ("abc123", True),
    ("abcabcd", False),
    ("abc!abc!", True),
    ("abc:abc", False),
]


@pytest.mark.parametrize(
    "word, expected", tests
)
def test_validate_word(word, expected):
    assert validate_word(word) == expected
