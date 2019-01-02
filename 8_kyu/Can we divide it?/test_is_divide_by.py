from is_divide_by import is_divide_by


def test_is_divide_by():
    assert is_divide_by(8, 2, 4) is True
    assert is_divide_by(12, -3, 4) is True
    assert is_divide_by(8, 3, 4) is False
    assert is_divide_by(48, 2, -5) is False
    assert is_divide_by(-100, -25, 10) is True
    assert is_divide_by(10000, 5, -3) is False
    assert is_divide_by(4, 4, 2) is True
    assert is_divide_by(5, 2, 3) is False
    assert is_divide_by(-96, 25, 17) is False
    assert is_divide_by(33, 1, 33) is True
