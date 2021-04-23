import pytest

from solution import count_adjacent_pairs


data = [
    ('', 0),
    ('orange Orange kiwi pineapple apple', 1),
    ('banana banana banana', 1),
    ('banana banana banana terracotta banana terracotta terracotta pie!', 2),
    ('pineapple apple', 0),
]


@pytest.mark.parametrize(
    "st, expected", data
)
def test_count_adjacent_pairs(st, expected):
    assert count_adjacent_pairs(st) == expected
