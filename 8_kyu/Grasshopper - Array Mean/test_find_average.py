from find_average import find_average


def test_find_average():
    assert find_average([1]) == 1
    assert find_average([1, 3, 5, 7]) == 4
    assert find_average([-1, 3, 5, -7]) == 0
    assert find_average([5, 7, 3, 7]) == 5.5
    assert find_average([]) == 0
