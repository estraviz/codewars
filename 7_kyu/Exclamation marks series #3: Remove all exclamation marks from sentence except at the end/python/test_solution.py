import pytest

from solution import remove


tests = [
    ('Hi!', 'Hi!'),
    ('Hi!!!', 'Hi!!!'),
    ('!Hi', 'Hi'),
    ('!Hi!', 'Hi!'),
    ('Hi! Hi!', 'Hi Hi!'),
    ('Hi', 'Hi'),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_remove(s, expected):
    assert remove(s) == expected
