import pytest

from solution import balance


tests = [
    ("", "", "Balance"),
    ("!!", "??", "Right"),
    ("!??", "?!!", "Left"),
    ("!?!!", "?!?", "Left"),
    ("!!???!????", "??!!?!!!!!!!", "Balance"),
]


@pytest.mark.parametrize(
    "left, right, expected", tests
)
def test_balance(left, right, expected):
    assert balance(left, right) == expected
