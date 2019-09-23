from is_nice import is_nice


def test_is_nice():
    assert is_nice([2, 10, 9, 3]) is True
    assert is_nice([3, 4, 5, 7]) is False
    assert is_nice([0, 2, 19, 4, 4]) is False
    assert is_nice([3, 2, 1, 0]) is True
    assert is_nice([3, 2, 10, 4, 1, 6]) is False
    assert is_nice([1, 1, 8, 3, 1, 1]) is False
    assert is_nice([0, 1, 2, 3]) is True
    assert is_nice([1, 2, 3, 4]) is True
    assert is_nice([0, -1, 1]) is True
    assert is_nice([0, 2, 3]) is False
    assert is_nice([0]) is False
    assert is_nice([]) is False
    assert is_nice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) is True
    assert is_nice([0, 1, 3, -2, 5, 4]) is False
    assert is_nice([0, -1, -2, -3, -4]) is True
    assert is_nice([1, -1, 3]) is False
    assert is_nice([1, -1, 2, -2, 3, -3, 6]) is False
    assert is_nice([2, 2, 3, 3, 3]) is True
    assert is_nice([1, 1, 1, 2, 1, 1]) is True
