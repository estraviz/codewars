import pytest

from solution import grabscrab


tests = [
    ("trisf", ["first"], ["first"]),
    ("oob", ["bob", "baobab"], []),
    ("ainstuomn", ["mountains", "hills", "mesa"], ["mountains"]),
    ("oolp", ["donkey", "pool", "horse", "loop"], ["pool", "loop"]),
    ("ortsp", ["sport", "parrot", "ports", "matey"], ["sport", "ports"]),
    ("ourf", ["one", "two", "three"], []),
]


@pytest.mark.parametrize(
    "word, possible_word, expected", tests
)
def test_grabscrab(word, possible_word, expected):
    assert grabscrab(word, possible_word) == expected
