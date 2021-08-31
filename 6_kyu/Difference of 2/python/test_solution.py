import pytest

from solution import twos_difference


basic_tests = [
    ([1, 2, 3, 4], [(1, 3), (2, 4)]),
    ([1, 3, 4, 6], [(1, 3), (4, 6)]),
    ([0, 3, 1, 4], [(1, 3)]),
    ([4, 1, 2, 3], [(1, 3), (2, 4)]),
    ([6, 3, 4, 1, 5], [(1, 3), (3, 5), (4, 6)]),
    ([3, 1, 6, 4], [(1, 3), (4, 6)]),
    ([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56], [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)]),
]


@pytest.mark.parametrize(
    "lst, expected", basic_tests
)
def test_basic_tests(lst, expected):
    assert twos_difference(lst) == expected


edge_tests = [
    ([1, 4, 7, 10], []),
    ([], []),
]

@pytest.mark.parametrize(
    "lst, expected", edge_tests
)
def test_basic_tests(lst, expected):
    assert twos_difference(lst) == expected