import pytest

from solution import tap_code_translation


data = [
    ("breaks", ". .. .... .. . ..... . . . ... .... ..."),
    ("taps", ".... .... . . ... ..... .... ..."),
    ("knocks", ". ... ... ... ... .... . ... . ... .... ..."),
    ("test", ".... .... . ..... .... ... .... ...."),
    ("total", ".... .... ... .... .... .... . . ... ."),
    ("break", ". .. .... .. . ..... . . . ..."),
    ("something", ".... ... ... .... ... .. . ..... .... .... .. ... .. .... ... ... .. .."),
    ("final", ".. . .. .... ... ... . . ... ."),
]


@pytest.mark.parametrize(
    "text, result", data
)
def test_tap_code_translation(text, result):
    assert tap_code_translation(text) == result
