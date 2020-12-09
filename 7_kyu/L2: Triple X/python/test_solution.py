import pytest

from solution import triple_x


@pytest.mark.parametrize(
    "actual, expected",
    [
        ("", False),
        ("there's no XXX here", False),
        ("abraxxxas", True),
        ("xoxotrololololololoxxx", False),
        ("soft kitty, warm kitty, xxxxx", True),
        ("softx kitty, warm kitty, xxxxx", False),
        ("Xabraxxxas", True),
        ("xoXotrololololololoxxx", False),
        ("softXxxx kitty, warm kitty, xxxxx", True),
        ("softxXxxx kitty, warm kitty, xxxxx", False),
    ],
)
def test_solution(actual, expected):
    assert triple_x(actual) == expected
