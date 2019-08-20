from crossing_sum import crossing_sum


def test_crossing_sum():
    assert crossing_sum([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]], 1, 3) == 12
    assert crossing_sum([[1, 1], [3, 3], [1, 1], [2, 2]], 3, 0) == 9
    assert crossing_sum([[100]], 0, 0) == 100
    assert crossing_sum([[1, 2, 3, 4, 5]], 0, 0) == 15
    assert crossing_sum([[1], [2], [3], [4], [5]], 0, 0) == 15
