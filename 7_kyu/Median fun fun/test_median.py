from median import median


def test_median():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([3, 4, 1, 2, 5]) == 3
    assert median([10, 29, 23, 94, 76, 96, 5, 85, 4, 33, 47, 41, 87]) == 41
    assert median([1]) == 1
    assert median([1, -1]) == 0
