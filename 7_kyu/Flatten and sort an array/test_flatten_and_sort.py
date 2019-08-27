from flatten_and_sort import flatten_and_sort


def test_flatten_and_sort():
    assert flatten_and_sort([]) == []
    assert flatten_and_sort([[], [1]]), [1]
    assert flatten_and_sort([[3, 2, 1], [7, 9, 8],
                             [6, 4, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten_and_sort([[1, 3, 5], [100],
                             [2, 4, 6]]) == [1, 2, 3, 4, 5, 6, 100]
