from swap_head_tail import swap_head_tail


def test_swap_head_tail():
    arr = [1, 2, 3, 4, 5]
    assert swap_head_tail(arr) == [4, 5, 3, 1, 2]

    arr = [-1, 2]
    assert swap_head_tail(arr) == [2, -1]

    arr = [1, 2, -3, 4, 5, 6, -7, 8]
    assert swap_head_tail(arr) == [5, 6, -7, 8, 1, 2, -3, 4]
