import pytest

from solution import remove_exclamation_marks

data = [
    ("Hello World!", "Hello World"),
    ("Hello World!!!", "Hello World"),
    ("Hi! Hello!", "Hi Hello"),
    ("", ""),
    ("!Hi! Hello!", "Hi Hello"),
    ("!Hi Hello!", "Hi Hello"),
    ("Hi! Hello!", "Hi Hello"),
    ("Oh, no!!!", "Oh, no"),
]

@pytest.mark.parametrize("s, result", data)
def test_remove_exclamation_marks(s, result):
    assert remove_exclamation_marks(s) == result
