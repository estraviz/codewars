from solution import kata_13_december


def test_basic_tests():
    assert kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]) == [1, 3, 5, 7]
    assert kata_13_december([1, 2, 2, 2, 4, 3, 4]) == [1, 3]
