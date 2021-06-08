import pytest

from solution import ordered_count


tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)


@pytest.mark.parametrize(
    "inp, expected", tests
)
def test_ordered_count(inp, expected):
    assert ordered_count(inp) == expected
