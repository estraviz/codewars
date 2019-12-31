from array_madness import array_madness


def test_array_madness():
    assert array_madness([4, 5, 6], [1, 2, 3]) is True
    assert array_madness([1, 2, 3], [4, 5, 6]) is False
    assert array_madness([4, 5, 6], [3, 4, 5]) is False
    assert array_madness([3, 4, 5], [2, 3, 4]) is False
    assert array_madness([2, 3, 4], [1, 2, 3]) is False
    assert array_madness([1, 2, 3], [0, 1, 2]) is True
    assert array_madness([5, 3, 2, 4, 1], [15]) is False
    assert array_madness([2, 5, 3, 4, 1], [3, 3, 3, 3, 3]) is False
    assert array_madness([1, 3, 4, 2, 4], [2, 2, 2, 2, 2, 2, 2, 1]) is False
    assert array_madness([1, 2, 3, 4, 5], [2, 2, 2, 2, 2, 2, 1, 1, 1]) is True
    assert array_madness([2, 4, 6, 8, 10, 12, 14],
                         [1, 3, 5, 7, 9, 11, 13]) is False
