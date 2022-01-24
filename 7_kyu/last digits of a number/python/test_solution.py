import pytest

from solution import solution


example_tests = [
    (1, 1, [1]),
    (123767, 4, [3, 7, 6, 7]),
    (0, 1, [0]),
    (34625647867585, 10, [5, 6, 4, 7, 8, 6, 7, 5, 8, 5]),
]


@pytest.mark.parametrize(
    "n, d, expected", example_tests
)
def test_example_tests(n, d, expected):
    assert solution(n, d) == expected


d_non_positive_tests = [
    (1234, 0, []),
    (24134, -4, []),
]

@pytest.mark.parametrize(
    "n, d, expected", d_non_positive_tests
)
def test_d_non_positive_tests(n, d, expected):
    assert solution(n, d) == expected


d_gt_num_digits_in_n_tests = [
    (1343, 5, [1, 3, 4, 3]),
]


@pytest.mark.parametrize(
    "n, d, expected", d_gt_num_digits_in_n_tests
)
def test_d_gt_num_digits_in_n_tests(n, d, expected):
    assert solution(n, d) == expected
