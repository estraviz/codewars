import pytest

from solution import max_redigit


basic_tests = [
    (123, 321),
    (555, 555),
]


@pytest.mark.parametrize(
    "num, expected", basic_tests
)
def test_basic(num, expected):
    assert max_redigit(num) == expected


edge_tests = [
    (-1, None),
    (0, None),
    (99, None),
    (1000, None),
]


@pytest.mark.parametrize(
    "num, expected", edge_tests
)
def test_edge(num, expected):
    assert max_redigit(num) == expected
