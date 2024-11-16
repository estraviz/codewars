from array_plus_array import array_plus_array


def test_array_plus_array():
    assert array_plus_array([1, 2, 3], [4, 5, 6]) == 21
    assert array_plus_array([-1, -2, -3], [-4, -5, -6]) == -21
    assert array_plus_array([0, 0, 0], [4, 5, 6]) == 15
    assert array_plus_array([100, 200, 300], [400, 500, 600]) == 2100
