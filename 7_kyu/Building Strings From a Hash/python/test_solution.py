import pytest

from solution import solution


data = [
    ({'a': 1, 'b': 2}, 'a = 1,b = 2'),
    ({'a': 'b', 'b': 'a'}, 'a = b,b = a'),
    ({0: 'a', 'b': 2}, '0 = a,b = 2'),
    ({'b': 1, 'c': 2, 'e': 3}, 'b = 1,c = 2,e = 3'),
    ({}, ''),
]


@pytest.mark.parametrize(
    "pairs, expected", data
)
def test_solution(pairs, expected):
    assert solution(pairs) == expected
