import pytest
from solution import longest_repetition


@pytest.mark.parametrize("data, expected", [
    ["aaaabb", ('a', 4)],
    ["bbbaaabaaaa", ('a', 4)],
    ["cbdeuuu900", ('u', 3)],
    ["abbbbb", ('b', 5)],
    ["aabb", ('a', 2)],
    ["ba", ('b', 1)],
    ["", ('', 0)],
])
def test_frequency(data, expected):
    assert longest_repetition(data) == expected
