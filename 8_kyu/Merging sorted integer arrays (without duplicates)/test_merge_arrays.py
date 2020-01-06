from merge_arrays import merge_arrays


def test_basic_tests():
    assert merge_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_arrays([2, 4, 8], [2, 4, 6]) == [2, 4, 6, 8]


def test_edge_case_tests():
    assert merge_arrays([1, 2, 3], []) == [1, 2, 3]
    assert merge_arrays([], []) == []
