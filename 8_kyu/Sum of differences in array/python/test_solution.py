from solution import sum_of_differences


def test_sample_tests():
    assert sum_of_differences([1, 2, 10]) == 9
    assert sum_of_differences([-3, -2, -1]) == 2
    assert sum_of_differences([1, 1, 1, 1, 1]) == 0
    assert sum_of_differences([-17, 17]) == 34
    assert sum_of_differences([]) == 0
    assert sum_of_differences([0]) == 0
    assert sum_of_differences([-1]) == 0
    assert sum_of_differences([1]) == 0
