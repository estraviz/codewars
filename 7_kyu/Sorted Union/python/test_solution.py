from solution import unite_unique


def test_sorted_union():
    assert unite_unique([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]) == [1, 3, 2, 5, 4]
    assert unite_unique([4, 3, 2, 2]) == [4, 3, 2]
    assert unite_unique([4, "a", 2], []) == [4, "a", 2]
    assert unite_unique([], [4, "a", 2]) == [4, "a", 2]
    assert unite_unique([], [4, "a", 2], []) == [4, "a", 2]
    assert unite_unique([]) == []
    assert unite_unique([], []) == []
    assert unite_unique([], [1, 2]) == [1, 2]
    assert unite_unique([], [1, 2, 1, 2], [2, 1, 1, 2, 1]) == [1, 2]
