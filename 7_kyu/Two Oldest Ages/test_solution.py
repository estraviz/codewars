import pytest
from solution import two_oldest_ages


@pytest.mark.parametrize(
    "ages, result",
    [
        [[1, 5, 87, 45, 8, 8], [45, 87]],
        [[6, 5, 83, 5, 3, 18], [18, 83]],
        [[10, 1], [1, 10]],
    ],
)
def test_two_oldest_ages(ages, result):
    assert two_oldest_ages(ages) == result
