import pytest

from solution import number_of_pairs


basic_tests = [
    (["red", "red"], 1),
    (["red", "green", "blue"], 0),
    (["gray", "black", "purple", "purple", "gray", "black"], 3),
    ([], 0),
    (["red", "green", "blue", "blue", "red", "green", "red", "red", "red"], 4),
]


@pytest.mark.parametrize(
    "gloves, expected", basic_tests
)
def test_should_count_number_of_pairs_for_basic_tests(gloves, expected):
    assert number_of_pairs(gloves) == expected
