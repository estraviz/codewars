from next_id import next_id


def test_next_id():
    assert next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert next_id([5, 4, 3, 2, 1]) == 0
    assert next_id([0, 1, 2, 3, 5]) == 4
    assert next_id([0, 0, 0, 0, 0, 0]) == 1
    assert next_id([]) == 0
    assert next_id([0, 0, 1, 1, 2, 2]) == 3
    assert next_id([0, 1, 1, 1, 3, 2]) == 4
    assert next_id([0, 1, 0, 2, 0, 3]) == 4
    assert next_id([9, 8, 0, 1, 7, 6]) == 2
    assert next_id([9, 8, 7, 6, 5, 4]) == 0
