import pytest

from solution import alphabet_war


tests = [
    ("z", "Right side wins!"),
    ("zdqmwpbs", "Let's fight again!"),
    ("wq", "Left side wins!"),
    ("zzzzs", "Right side wins!"),
    ("wwwwww", "Left side wins!"),
]

@pytest.mark.parametrize(
    "fight, expected", tests
)
def test_alphabet_war(fight, expected):
    assert alphabet_war(fight) == expected
