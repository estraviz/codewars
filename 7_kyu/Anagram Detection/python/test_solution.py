import pytest

from solution import is_anagram


data = [
    ("foefet", "toffee", True),
    ("Buckethead", "DeathCubeK", True),
    ("Twoo", "WooT", True),
    ("dumble", "bumble", False),
    ("ound", "round", False),
    ("apple", "pale", False),
]


@pytest.mark.parametrize(
    "test, original, result", data
)
def test_is_anagram(test, original, result):
    assert is_anagram(test, original) == result
