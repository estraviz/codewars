from is_prime import is_prime


def test_is_prime_small_numbers():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(41) is True
    assert is_prime(45) is False
    assert is_prime(73) is True
    assert is_prime(75) is False


def test_is_prime_bigger_number():
    assert is_prime(5099) is True


def test_is_prime_negative_number():
    assert is_prime(-1) is False
