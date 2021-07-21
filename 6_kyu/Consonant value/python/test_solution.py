import pytest

from solution import solve


tests = [
    ("zodiac", 26),
    ("chruschtschov", 80),
    ("khrushchev", 38),
    ("strength", 57),
    ("catchphrase", 73),
    ("twelfthstreet", 103),
    ("mischtschenkoana", 80),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_solve(s, expected):
    assert solve(s) == expected
