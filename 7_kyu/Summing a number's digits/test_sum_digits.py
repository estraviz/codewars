from sum_digits import sum_digits


def test_sum_digits():
    assert sum_digits(10) == 1
    assert sum_digits(99) == 18
    assert sum_digits(-32) == 5
    assert sum_digits(1234567890) == 45
    assert sum_digits(0) == 0
    assert sum_digits(666) == 18
    assert sum_digits(100000002) == 3
    assert sum_digits(800000009) == 17
