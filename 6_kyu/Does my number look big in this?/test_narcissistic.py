from narcissistic import narcissistic
from random import randint


def test_small_narcissistic():
    assert narcissistic(1) is True
    assert narcissistic(5) is True
    assert narcissistic(7) is True


def test_large_narcissistic():
    assert narcissistic(153) is True
    assert narcissistic(370) is True
    assert narcissistic(371) is True
    assert narcissistic(1634) is True


def test_no_narcissistic():
    for a in range(10):
        num = randint(5, 9) * 60000 + randint(1, 99)
        assert narcissistic(num) is False


bignums = [8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817,
           9926315, 24678050, 24678051]


def test_big_nums():
    for b in bignums:
        if randint(0, 10) > 5:
            assert narcissistic(b) is True
        else:
            num = randint(5, 9) * 900000 + randint(1, 99)
            assert narcissistic(num) is False
