from shuffled_array import shuffled_array


def test_shuffled_array():
    assert shuffled_array([1, 12, 3, 6, 2]) == [1, 2, 3, 6]
    assert shuffled_array([1, -3, -5, 7, 2]) == [-5, -3, 2, 7]
    assert shuffled_array([2, -1, 2, 2, -1]) == [-1, -1, 2, 2]
    assert shuffled_array([-3, -3]) == [-3]
