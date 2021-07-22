import pytest

from solution import shorter_reverse_longer


tests = [
    ("first", "abcde", "abcdetsrifabcde"),
    ("hello", "bau", "bauollehbau"),
    ("abcde", "fghi", "fghiedcbafghi"),
]


@pytest.mark.parametrize(
    "a, b, expected", tests
)
def test_shorter_reverse_longer(a, b, expected):
    assert shorter_reverse_longer(a, b) == expected
