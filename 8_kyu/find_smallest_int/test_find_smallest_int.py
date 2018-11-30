from find_smallest_int import find_smallest_int


def test_find_smallest_int():
    assert find_smallest_int([78, 56, 232, 12, 11, 43]) == 11
    assert find_smallest_int([78, 56, -2, 12, 8, -33]) == -33
    assert find_smallest_int([0, 1-2**64, 2**64]) == 1-2**64

    assert find_smallest_int([-133, -5666, -89, -12341,
                                                -321423, 2**64]) == -321423

    assert find_smallest_int([0, 2**64, -1-2**64, 2**64, 2**64]) == -1-2**64
    assert find_smallest_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert find_smallest_int([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -10
    assert find_smallest_int([-78, 56, 232, 12, 8]) == -78
    assert find_smallest_int([78, 56, -2, 12, -8]) == -8
