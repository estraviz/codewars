from sum_even_fibonacci import sum_even_fibonacci


def test_sum_even_fibonacci():
    assert sum_even_fibonacci(1) == 0
    assert sum_even_fibonacci(2) == 2
    assert sum_even_fibonacci(8) == 10
    assert sum_even_fibonacci(111111) == 60696
    assert sum_even_fibonacci(8675309) == 4613732
    assert sum_even_fibonacci(144100000) == 82790070
    assert sum_even_fibonacci(65140000) == 82790070
    assert sum_even_fibonacci(7347000000) == 6293134512
    assert sum_even_fibonacci(10000000000000) == 8583840088782
    assert sum_even_fibonacci(123456789000000) == 154030760585064
