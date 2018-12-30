from hex_to_dec import hex_to_dec
from random import randint


def test_hex_to_dec_simple_tests():
    assert hex_to_dec("1") == 1
    assert hex_to_dec("a") == 10
    assert hex_to_dec("10") == 16


def test_hex_to_dec_random_tests():
    for _ in range(100):
        num = randint(0, 20000)
        hex_num = hex(num)[2:]
        assert hex_to_dec(hex_num) == num
