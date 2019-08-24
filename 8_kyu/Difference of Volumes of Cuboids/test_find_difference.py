from find_difference import find_difference


def test_find_difference():
    assert find_difference([3, 2, 5], [1, 4, 4]) == 14
    assert find_difference([9, 7, 2], [5, 2, 2]) == 106
