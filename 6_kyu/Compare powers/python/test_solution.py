import pytest

from solution import compare_powers


tests_smaller_numbers = [
    ([2, 10], [2, 15], 1),
    ([2, 10], [3, 10], 1),
    ([2, 10], [2, 10], 0),
    ([3, 9], [5, 6], -1),
    ([7, 7], [5, 8], -1),
]


@pytest.mark.parametrize(
    "n1, n2, expected", tests_smaller_numbers
)
def test_compare_powers_for_smaller_numbers(n1, n2, expected):
    assert compare_powers(n1, n2) == expected


tests_larger_numbers = [
    ([2, 100], [2, 150], 1),
    ([2, 100], [3, 100], 1),
    ([2, 100], [2, 100], 0),
    ([34, 98], [51, 67], -1),
    ([1024, 97], [1024, 81], -1),
]


@pytest.mark.parametrize(
    "n1, n2, expected", tests_larger_numbers
)
def test_compare_powers_for_larger_numbers(n1, n2, expected):
    assert compare_powers(n1, n2) == expected
