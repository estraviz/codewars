import pytest

from solution import sabb


tests = [
    ("Can I have a sabbatical?", 5, 5, "Sabbatical! Boom!"),
    ("Why are you shouting?", 7, 2, "Back to your desk, boy."),
    ("What do you mean I cant learn to code??", 8, 9, "Sabbatical! Boom!"),
    ("Please calm down", 9, 1, "Back to your desk, boy."),
    ("I can?! Nice. FaC..Im coming :D", 9, 9, "Sabbatical! Boom!"),
]


@pytest.mark.parametrize(
    "s, val, happiness, expected", tests
)
def test_sabbatical(s, val, happiness, expected):
    assert sabb(s, val, happiness) == expected
