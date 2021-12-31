import pytest

from solution import same_case


tests = [
    ('C', 'B', 1),
    ('b', 'a', 1),
    ('d', 'd', 1),
    ('A', 's', 0),
    ('c', 'B', 0),
    ('b', 'Z', 0),
    ('\t', 'Z', -1),
    ('H', ':', -1),
]


@pytest.mark.parametrize(
    "a, b, expected", tests
)
def test_same_case(a, b, expected):
    assert same_case(a, b) == expected
