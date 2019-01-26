from sum_array import sum_array


def test_none_or_empty():
    assert sum_array(None) == 0
    assert sum_array([]) == 0


def test_only_one_element():
    assert sum_array([3]) == 0
    assert sum_array([-3]) == 0


def test_only_two_element():
    assert sum_array([3, 5]) == 0
    assert sum_array([-3, -5]) == 0


def test_real_tests():
    assert sum_array([6, 2, 1, 8, 10]) == 16
    assert sum_array([6, 0, 1, 10, 10]) == 17
    assert sum_array([-6, -20, -1, -10, -12]) == -28
    assert sum_array([-6, 20, -1, 10, -12]) == 3
