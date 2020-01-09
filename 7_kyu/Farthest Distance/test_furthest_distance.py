from furthest_distance import furthest_distance


def test_furthest_distance():
    assert furthest_distance([[3, 8], [10, 4]]) == 8.06
    assert furthest_distance([[1, 1], [2, 3], [5, 5], [4, 3], [3, 3], [4, 1],
                              [2, 2]]) == 5.66
    assert furthest_distance([[1, 2], [3, 8], [4, 3]]) == 6.32
    assert furthest_distance([[33, 33], [33, 33], [33, 33], [33, 33],
                              [33, 33]]) == 0.0
