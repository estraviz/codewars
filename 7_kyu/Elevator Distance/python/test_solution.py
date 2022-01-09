import pytest

from solution import elevator_distance


tests = [
    ([5, 2, 8], 9),
    ([1, 2, 3], 2),
    ([7, 1, 7, 1], 18),
]


@pytest.mark.parametrize(
    "array, expected", tests
)
def test_elevator_distance(array, expected):
    assert elevator_distance(array) == expected
