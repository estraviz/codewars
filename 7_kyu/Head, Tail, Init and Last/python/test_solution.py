from solution import head, tail, init, last


def test_head_tail_init_last():
    assert head([5, 1]) == 5
    assert tail([1]) == []
    assert init([1, 5, 7, 9]) == [1, 5, 7]
    assert last([7, 2]) == 2
