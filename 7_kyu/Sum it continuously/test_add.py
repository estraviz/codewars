from add import add


def test_add():
    assert add([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
    assert add([20, 21, 22, 23, 24, 25]) == [20, 41, 63, 86, 110, 135]
    assert add([2, 4, 6, 8, 10]) == [2, 6, 12, 20, 30]
    assert add([6, 7, 8, 9, 10, 'a', 'z']) == 'Invalid input'
    assert add([1, 4, 9, 16, 25, 36]) == [1, 5, 14, 30, 55, 91]
    assert add('Invalid input') == 'Invalid input'
    assert add([1, 2, 'a', '6', 3, 6, 's']) == 'Invalid input'
    assert add([1, 8, 27, 64, 125]) == [1, 9, 36, 100, 225]
