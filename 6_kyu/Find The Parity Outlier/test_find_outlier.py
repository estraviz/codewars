import sys
from find_outlier import find_outlier


def test_simple():
    assert find_outlier([0, 1, 2]) == 1
    assert find_outlier([1, 2, 3]) == 2


def test_more_complex():
    ints1 = [2, 6, 8, 10, 3]  # odd at the back
    ints2 = [2, 6, 8, 200, 700, 1, 84, 10, 4]  # odd in the middle
    ints3 = [17, 6, 8, 10, 6, 12, 24, 36]  # odd in the front
    ints4 = [2, 1, 7, 17, 19, 211, 7]  # even in the front
    ints5 = [1, 1, 1, 1, 1, 44, 7, 7, 7, 7, 7, 7, 7, 7]  # even in the middle
    ints6 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 35, 5, 5, 5, 5, 5, 5, 5,
             5, 5, 5, 7, 7, 7, 7, 1000]  # even at the end
    ints7 = [2, -6, 8, -10, -3]  # odd at the back,  negative
    ints8 = [2, 6, 8, 2, -66, 34, -35, 66, 700, 1002, -84, 10, 4]  # odd in the middle,  negative
    ints9 = [-1 * sys.maxsize, -18, 6, -8, -10, 6, 12, -24, 36]  # odd in the front,  negative
    ints10 = [-20, 1, 7, 17, 19, 211, 7]  # even in the front,  negative
    ints11 = [1, 1, -1, 1, 1, -44, 7, 7, 7, 7, 7, 7, 7, 7]  # even in the middle,  negative
    ints12 = [1, 0, 0]  # odd answer,  zeroes
    ints13 = [3, 7, -99, 81, 90211, 0, 7]  # even in the middle,  zero

    inputs = [ints1, ints2, ints3, ints4, ints5, ints6, ints7, ints8, ints9,
              ints10, ints11, ints12, ints13]
    expected = [3, 1, 17, 2, 44, 1000, -3, -35, -1*sys.maxsize, -20, -44, 1, 0]

    for i, (ins, e) in enumerate(zip(inputs, expected)):
        assert find_outlier(ins) == e
