from solution import alphabet


def test_basic_tests():
    assert alphabet([2, 3, 4, 1, 12, 6, 2, 4]) == 4
    assert alphabet([2, 6, 7, 3, 14, 35, 15, 5]) == 7
    assert alphabet([20, 10, 6, 5, 4, 3, 2, 12]) == 5
    assert alphabet([2, 6, 18, 3, 6, 7, 42, 14]) == 7
    assert alphabet([7, 96, 8, 240, 12, 140, 20, 56]) == 20
    assert alphabet([20, 30, 6, 7, 4, 42, 28, 5]) == 7
