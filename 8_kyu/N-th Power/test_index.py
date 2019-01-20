from index import index


def test_index():
    assert index([1, 2, 3, 4], 2) == 9
    assert index([1, 3, 10, 100], 3) == 1000000
    assert index([0, 1], 0) == 1
    assert index([1, 2], 3) == -1
    assert index([0], 0) == 1
    assert index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9) == 1
    assert index([1, 1, 1, 1, 1, 1, 1, 1, 1, 100], 9) == 1000000000000000000
    assert index([29, 82, 45, 10], 3) == 1000
    assert index([6, 31], 3) == -1
    assert index([75, 68, 35, 61, 9, 36, 89, 0, 30], 10) == -1
