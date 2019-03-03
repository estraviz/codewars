from is_square import is_square


def test_is_square():
    assert is_square(-1) is False
    assert is_square(0) is True
    assert is_square(3) is False
    assert is_square(4) is True
    assert is_square(25) is True
    assert is_square(26) is False
