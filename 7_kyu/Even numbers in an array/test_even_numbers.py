from even_numbers import even_numbers


def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [4, 6, 8]
    assert even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) == \
        [-8, 26]
    assert even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) == [6]
