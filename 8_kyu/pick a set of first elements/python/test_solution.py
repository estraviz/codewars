import pytest

from solution import first


s = ['a', 'b', 'c', 'd', 'e']
data = [
    ((s, ), ['a']),
    ((s, 0), []),
    ((s, 1), ['a']),
    ((s, 2), ['a', 'b']),
    ((s, 10), ['a', 'b', 'c', 'd', 'e']),
]


@pytest.mark.parametrize(
    'args, expected', data
)
def test_first(args, expected):
    assert first(*args) == expected
