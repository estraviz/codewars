from sum_mul import sum_mul


def test_basic_examples():
    assert sum_mul(4, 123) == 1860
    assert sum_mul(123, 4567) == 86469


def test_should_not_include_m():
    assert sum_mul(2, 10) == 20


def test_should_not_work_for_n_equal_m():
    assert sum_mul(2, 2) == 0
    assert sum_mul(7, 7) == 0


def test_should_work_for_n_greater_than_m():
    assert sum_mul(7, 2) == 0
    assert sum_mul(21, 3) == 0


def test_zero_is_not_a_natural_number_for_this_kata():
    assert sum_mul(0, 2) == 'INVALID'
    assert sum_mul(2, 0) == 'INVALID'


def test_negative_numbers():
    assert sum_mul(4, -7) == 'INVALID'
    assert sum_mul(-7, 4) == 'INVALID'
