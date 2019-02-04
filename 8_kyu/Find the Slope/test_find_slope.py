from find_slope import find_slope


def test_undefined_results():
    assert find_slope([17, -3, 17, 8]) == "undefined"
    assert find_slope([15, -3, 15, -3]) == "undefined"
    assert find_slope([4, 16, 4, 18]) == "undefined"
    assert find_slope([-6, 57, -6, 84]) == "undefined"
    assert find_slope([90, 54, 90, 2]) == "undefined"


def test_negative_results():
    assert find_slope([1, -19, -2, -7]) == "-4"
    assert find_slope([9, 3, 19, -17]) == "-2"
    assert find_slope([2, 7, 4, -7]) == "-7"
    assert find_slope([18, -36, 12, 36]) == "-12"
    assert find_slope([36, 580, 42, 40]) == "-90"


def test_positive_results():
    assert find_slope([3, -20, 5, 8]) == "14"
    assert find_slope([6, -12, 15, -3]) == "1"
    assert find_slope([3, 6, 4, 10]) == "4"
    assert find_slope([1, 24, 2, 88]) == "64"
    assert find_slope([4, 384, 8, 768]) == "96"
    assert find_slope([7, 28, 9, 64]) == "18"
    assert find_slope([1, 2, 2, 6]) == "4"
    assert find_slope([92, 12, 96, 64]) == "13"
    assert find_slope([1, 2, 2, 6]) == "4"
    assert find_slope([3, 6, 4, 9]) == "3"
    assert find_slope([-2, -5, 2, 3]) == "2"
    assert find_slope([3, 3, 2, 0]) == "3"


def test_slope_is_zero():
    assert find_slope([12, -18, -15, -18]) == "0"
    assert find_slope([19, 3, 20, 3]) == "0"
