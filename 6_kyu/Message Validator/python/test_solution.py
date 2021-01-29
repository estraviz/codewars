import pytest

from solution import is_a_valid_message


data = [
    ("3hey5hello2hi", True),
    ("4code13hellocodewars", True),
    ("3hey5hello2hi5", False),
    ("code4hello5", False),
    ("1a2bb3ccc4dddd5eeeee", True),
    ("", True),
]


@pytest.mark.parametrize("message, result", data)
def test_is_a_valid_message(message, result):
    assert is_a_valid_message(message) == result
