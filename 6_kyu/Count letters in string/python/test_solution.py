import pytest

from solution import letter_count


tests = [
    ("codewars", {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}),
    ("activity", {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1}),
    ("arithmetics", {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}),
    ("traveller", {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1}),
    ("daydreamer", {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1}),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_letter_count(s, expected):
    assert letter_count(s) == expected
