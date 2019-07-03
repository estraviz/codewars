from find import find


def test_find():
    assert find(5) == 8
    assert find(10) == 33
    assert find(100) == 2418
    assert find(1000) == 234168
