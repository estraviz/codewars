import pytest

from solution import fusc


tests = [
    (0, 0),
    (1, 1),
    (85, 21),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_fusc(n, expected):
    assert fusc(n) == expected

    results = [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3]
    for num, result in zip(range(21), results):
        assert fusc(num) == result
