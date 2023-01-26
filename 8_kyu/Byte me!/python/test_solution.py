from solution import total_bytes


def test_basic_tests():
    assert total_bytes("hello") == 54
    assert total_bytes(123) == 28
    assert total_bytes('[":)", 1]') == 58
    assert total_bytes({'john': 19}) == 232


def test_bigger_tests():
    assert total_bytes("¡◢龘") == 80
    assert total_bytes(999_999) == 28
    assert total_bytes((1,2)) == 56
    assert total_bytes("㋛"*12345) == 24764
