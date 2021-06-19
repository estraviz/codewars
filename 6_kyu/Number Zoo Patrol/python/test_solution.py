import pytest
from random import randint as R, shuffle as S

from solution import find_missing_number


tests_normal = [
    ([2, 3, 4], 1),
    ([1, 3, 4], 2),
    ([1, 2, 4], 3),
    ([1, 2, 3], 4),
]


@pytest.mark.parametrize(
    "numbers, expected", tests_normal
)
def test_should_find_missing_number_for_normal_tests(numbers, expected):
    assert find_missing_number(numbers) == expected


tests_edge = [
    ([], 1),
    ([1], 2),
    ([2], 1),
]


@pytest.mark.parametrize(
    "numbers, expected", tests_edge
)
def test_should_find_missing_number_for_edge_cases(numbers, expected):
    assert find_missing_number(numbers) == expected


def test_should_find_missing_number_for_big_tests():
    a = list(range(1, 10001))
    a.remove(36)
    assert find_missing_number(a) == 36

    a = list(range(1, 10001))
    a.remove(5112)
    assert find_missing_number(a) == 5112

    a = list(range(1, 10001))
    a.remove(9999)
    assert find_missing_number(a) == 9999


def test_should_find_missing_number_for_random_normal_tests():
    for _ in range(100):
        a = list(range(1, R(1, 200)))
        S(a)
        n = a.pop() if a else 1
        assert find_missing_number(a) == n


def test_should_find_missing_number_for_random_performance_tests():
    base = list(range(1, 1000001))
    S(base)
    for _ in range(20):
        n = R(1, 1000000)
        a = base[:]
        a.remove(n)
        assert find_missing_number(a) == n
