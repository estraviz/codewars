from is_divisible import is_divisible


def test_is_divisible():
    assert is_divisible(3, 3, 4) is False
    assert is_divisible(12, 3, 4) is True
    assert is_divisible(8, 3, 4) is False
    assert is_divisible(48, 3, 4) is True
    assert is_divisible(100, 5, 10) is True
    assert is_divisible(100, 5, 3) is False
    assert is_divisible(4, 4, 2) is True
    assert is_divisible(5, 2, 3) is False
    assert is_divisible(17, 17, 17) is True
    assert is_divisible(17, 1, 17) is True
