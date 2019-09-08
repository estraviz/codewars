from odd_one import odd_one


def test_odd_one():
    assert odd_one([2, 4, 6, 7, 10]) == 3
    assert odd_one([2, 16, 98, 10, 13, 78]) == 4
    assert odd_one([4, -8, 98, -12, -7, 90, 100]) == 4
    assert odd_one([2, 4, 6, 8]) == -1
