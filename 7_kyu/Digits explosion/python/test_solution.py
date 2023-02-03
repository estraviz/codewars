import pytest

from solution import explode


tests = [
    ("312", "333122"),
    ("102269", "12222666666999999999"),
    ("0", ""),
    ("000", ""),
    ("123", "122333")
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_explode(s, expected):
    assert explode(s) == expected
