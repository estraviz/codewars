from find_uniq import find_uniq


def test_basic_numbers():
    assert find_uniq([1, 1, 1, 2, 1, 1]) == 2
    assert find_uniq([0, 0, 0.55, 0, 0]) == 0.55


def test_basic_shuffled():
    assert find_uniq([4, 4, 4, 3, 4, 4, 4, 4]) == 3
    assert find_uniq([5, 5, 5, 5, 4, 5, 5, 5]) == 4
    assert find_uniq([6, 6, 6, 6, 6, 5, 6, 6]) == 5
    assert find_uniq([7, 7, 7, 7, 7, 7, 6, 7]) == 6


def test_last_item():
    assert find_uniq([8, 8, 8, 8, 8, 8, 8, 7]) == 7
    assert find_uniq([3, 3, 3, 3, 3, 3, 3, 2]) == 2
    assert find_uniq([2, 2, 2, 2, 2, 2, 2, 1]) == 1


def test_first_item():
    assert find_uniq([0, 1, 1, 1, 1, 1, 1, 1]) == 0
