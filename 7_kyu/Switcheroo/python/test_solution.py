import pytest

from solution import switcheroo


tests = [
    ("abc", "bac"),
    ('aaabcccbaaa', 'bbbacccabbb'),
    ('ccccc', 'ccccc'),
    ('abababababababab', 'babababababababa'),
    ('aaaaa', 'bbbbb'),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_switcheroo(s, expected):
    assert switcheroo(s) == expected
