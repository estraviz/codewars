from sort_array import sort_array


def test_sort_array():
    assert sort_array([5, 3, 2, 8, 1, 4, 11]) == [1, 3, 2, 8, 5, 4, 11]
    assert sort_array([2, 22, 37, 11, 4, 1, 5, 0]) == \
        [2, 22, 1, 5, 4, 11, 37, 0]
    assert sort_array([1, 111, 11, 11, 2, 1, 5, 0]) == \
        [1, 1, 5, 11, 2, 11, 111, 0]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == \
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == \
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]) == \
        [0, 1, 2, 3, 4, 5, 8, 7, 6, 9]
