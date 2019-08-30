from min_value import min_value


def test_min_value():
    assert min_value([1, 3, 1]) == 13
    assert min_value([4, 7, 5, 7]) == 457
    assert min_value([4, 8, 1, 4]) == 148
    assert min_value([5, 7, 9, 5, 7]) == 579
    assert min_value([6, 7, 8, 7, 6, 6]) == 678
    assert min_value([5, 6, 9, 9, 7, 6, 4]) == 45679
    assert min_value([1, 9, 1, 3, 7, 4, 6, 6, 7]) == 134679
    assert min_value([3, 6, 5, 5, 9, 8, 7, 6, 3, 5, 9]) == 356789
