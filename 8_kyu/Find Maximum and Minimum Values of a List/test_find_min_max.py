from find_min_max import min, max


def test_find_fixed_min():
    assert min([-52, 56, 30, 29, -54, 0, -110]) == -110
    assert min([42, 54, 65, 87, 0]) == 0
    assert min([1, 2, 3, 4, 5, 10]) == 1
    assert min([-1, -2, -3, -4, -5, -10]) == -10
    assert min([9]) == 9


def test_find_fixed_max():
    assert max([-52, 56, 30, 29, -54, 0, -110]) == 56
    assert max([4, 6, 2, 1, 9, 63, -134, 566]) == 566
    assert max([5]) == 5
    assert max([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]) == 555
    assert max([9]) == 9
