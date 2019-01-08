from sum_array import sum_array


def test_sum_array():
    assert sum_array([]) == 0
    assert sum_array([1, 2, 3]) == 6
    assert sum_array([1.1, 2.2, 3.3]) == 6.6
    assert sum_array([4, 5, 6]) == 15
    assert sum_array(range(101)) == 5050
