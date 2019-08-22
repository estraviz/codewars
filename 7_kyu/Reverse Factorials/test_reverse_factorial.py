from reverse_factorial import reverse_factorial


def test_static_cases():
    assert reverse_factorial(120) == '5!'
    assert reverse_factorial(3628800) == '10!'
    assert reverse_factorial(150) == 'None'


def test_random_tests():
    from random import shuffle, randint

    my_factorials_341 = [
        1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,
        479001600, 6227020800, 87178291200, 1307674368000
    ]

    test_cases = my_factorials_341 * 2 + [
        randint(3, 1307674368000) for _ in range(50)
    ]
    shuffle(test_cases)

    for num in test_cases:
        if num in my_factorials_341:
            test_exp = str(my_factorials_341.index(num) + 1) + '!'
        else:
            test_exp = 'None'
        assert reverse_factorial(num) == test_exp
