from validate_code import validate_code
from random import randint


def test_basic_tests():
    assert validate_code(123) is True
    assert validate_code(248) is True
    assert validate_code(8) is False
    assert validate_code(321) is True
    assert validate_code(9453) is False


def test_random_test():
    for _ in range(40):
        code = int(str(randint(1, 6)) + str(randint(1, 10**randint(1, 9))))
        assert validate_code(code) == validate_sol(code)


def validate_sol(code):
    return str(code)[0] in "123"
