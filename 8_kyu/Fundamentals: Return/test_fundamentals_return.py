from fundamentals_return import add, multiply, divide, mod, exponent, subt


def test_normal_tests():
    assert add(1, 2) == 3
    assert multiply(1, 2) == 2
    assert divide(2, 1) == 2
    assert mod(1, 2) == 1
    assert exponent(1, 2) == 1
    assert subt(1, 2) == -1


def test_validation_tests():
    assert add(5, 7) == 12
    assert multiply(5, 2) == 10
    assert divide(40, 10) == 4
    assert mod(5, 10) == 5
    assert exponent(2, 10) == 1024
    assert subt(5832, 1832) == 4000
