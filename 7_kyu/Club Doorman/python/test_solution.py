import pytest

from solution import pass_the_door_man


tests = [
    ("lettuce", 60),
    ("hill", 36),
    ("apple", 48),
]


@pytest.mark.parametrize(
    "word, expected", tests
)
def test_pass_the_door_man(word, expected):
    assert pass_the_door_man(word) == expected
