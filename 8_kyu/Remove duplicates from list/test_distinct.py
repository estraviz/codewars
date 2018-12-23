from distinct import distinct


def test_distinct():
    assert distinct([1]) == [1]
    assert distinct([1, 2]) == [1, 2]
    assert distinct([1, 1, 2]) == [1, 2]
    assert distinct([1, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    seq = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]
    assert distinct(seq) == [1, 2, 3, 4, 5, 6, 7]
