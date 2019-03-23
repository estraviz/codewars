from backwards_prime import backwards_prime


def test_backwards_prime():
    assert backwards_prime(2, 100) == [13, 17, 31, 37, 71, 73, 79, 97]
    assert backwards_prime(9900, 10000) == [9923, 9931, 9941, 9967]
    assert backwards_prime(501, 599) == []
    assert backwards_prime(7000, 7100) == [7027, 7043, 7057]

    a = [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]
    assert backwards_prime(70000, 70245) == a

    assert backwards_prime(70485, 70600) == [70489, 70529, 70573, 70589]
    assert backwards_prime(60000, 70000) == []

    b = [109537, 109579, 109583, 109609, 109663]
    assert backwards_prime(109500, 109700) == b

    c = [1095047, 1095209, 1095319, 1095403]
    assert backwards_prime(1095000, 1095403) == c

    d = [107, 113, 149, 157, 167, 179, 199, 311, 337, 347, 359, 389]
    assert backwards_prime(100, 403) == d

    assert backwards_prime(400, 503) == []
    assert backwards_prime(7048500, 7048600) == [7048519, 7048579]
    assert backwards_prime(1048500, 1048600) == [1048571, 1048583]
    assert backwards_prime(1000001, 1000100) == [1000033, 1000037, 1000039]
    assert backwards_prime(700000008, 700000050) == [700000031]
