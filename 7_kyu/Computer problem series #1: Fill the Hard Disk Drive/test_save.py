from save import save


def test_save():
    assert save([4, 4, 4, 3, 3], 12) == 3
    assert save([4, 4, 4, 3, 3], 11) == 2
    assert save([4, 8, 15, 16, 23, 42], 108) == 6
    assert save([13], 13) == 1
    assert save([1, 2, 3, 4], 250) == 4
    assert save([100], 500) == 1
    assert save([11, 13, 15, 17, 19], 8) == 0
    assert save([45], 12) == 0
