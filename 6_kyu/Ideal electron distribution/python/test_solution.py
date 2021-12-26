import pytest

from solution import atomic_number


tests = [
    (1, [1]),
    (10, [2, 8]),
    (11, [2, 8, 1]),
    (22, [2, 8, 12]),
    (23, [2, 8, 13]),
    (47, [2, 8, 18, 19]),
    (50, [2, 8, 18, 22]),
    (52, [2, 8, 18, 24]),
    (60, [2, 8, 18, 32]),
    (61, [2, 8, 18, 32, 1]),
]


@pytest.mark.parametrize(
    "electrons, expected", tests
)
def test_atomic_number(electrons, expected):
    assert atomic_number(electrons) == expected
