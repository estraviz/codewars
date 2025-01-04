import pytest

from solution import get_average

data = [
    ([2, 2, 2, 2], 2),
    ([1, 5, 87, 45, 8, 8], 25),
    ([2,5,13,20,16,16,10], 11),
    ([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7], 11),
    ([1], 1),
]

@pytest.mark.parametrize(
    "marks, result", data
)
def test_get_average(marks, result):
    assert get_average(marks) == result
