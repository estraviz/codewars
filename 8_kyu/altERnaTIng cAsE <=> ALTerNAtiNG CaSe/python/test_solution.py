import pytest

from solution import to_alternating_case

data = [
    ("hello world", "HELLO WORLD"),
    ("HELLO WORLD", "hello world"),
    ("hello WORLD", "HELLO world"),
    ("HeLLo WoRLD", "hEllO wOrld"),
    ("12345", "12345"),
    ("1a2b3c4d5e", "1A2B3C4D5E"),
    ("String.prototype.toAlternatingCase", "sTRING.PROTOTYPE.TOaLTERNATINGcASE"),
    ("Hello World", "hELLO wORLD"),
]

@pytest.mark.parametrize("s, result", data)
def test_to_alternating_case(s, result):
    assert to_alternating_case(s) == result
