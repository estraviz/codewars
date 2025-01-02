from find_average import find_average
from statistics import mean


def test_find_average():
    array = [17, 16, 16, 16, 16, 15, 17, 17, 15, 5, 17, 17, 16]
    assert find_average(array) == mean(array)
