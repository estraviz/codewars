import pytest

from solution import sortme


fixed_tests = [
    (["Hello", "there", "I'm", "fine"], ["fine", "Hello", "I'm", "there"]),
    (["C", "d", "a", "B"], ["a", "B", "C", "d"]),
    (["CodeWars"], ["CodeWars"]),
]


@pytest.mark.parametrize(
    "words, expected", fixed_tests
)
def test_fixed_tests(words, expected):
    assert sortme(words) == expected
