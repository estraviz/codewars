from solution import sum_args


def test_sum_args():
    assert sum_args(1) == 1
    assert sum_args(1, 2) == 3
    assert sum_args(5, 7, 9) == 21
    assert sum_args(12, 1, 1, 1, 1) == 16
    assert sum_args(12, 1, 1, 1, 1, 1, 1) == 18
