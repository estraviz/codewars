from ones_counter import ones_counter


def test_ones_counter():
    assert ones_counter([0]) == []
    assert ones_counter([1, 0, 1, 1]) == [1, 2]
    assert ones_counter([0, 0, 0, 0, 0, 0, 0, 0]) == []
    assert ones_counter([1, 1, 1, 1, 1]) == [5]
    assert ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]) == [3, 1, 2]
    assert ones_counter([0, 0, 0, 1, 0, 0, 1, 1]) == [1, 2]
    assert ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0,
                         1]) == [1, 2, 4, 1]
