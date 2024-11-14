from find_difference import find_difference


def test_find_difference():
    assert find_difference([3, 2, 5], [1, 4, 4]) == 14
    assert find_difference([9, 7, 2], [5, 2, 2]) == 106
    assert find_difference([11, 2, 5], [1, 10, 8]) == 30
    assert find_difference([4, 4, 7], [3, 9, 3]) == 31
    assert find_difference([15, 20, 25], [10, 30, 25]) == 0
