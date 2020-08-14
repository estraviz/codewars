from word_pattern import word_pattern
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [
        ("hello", "0.1.2.2.3"),
        ("heLlo", "0.1.2.2.3"),
        ("helLo", "0.1.2.2.3"),
        ("Hippopotomonstrosesquippedaliophobia",
            "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13"),
    ],
)
def test_word_pattern(test_input, expected):
    assert word_pattern(test_input) == expected
