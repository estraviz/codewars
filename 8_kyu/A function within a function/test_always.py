from always import always
import random


def test_always_undefined_n():
    assert always()() == 0


def test_always_random_n():
    for i in range(0, 10):
        num = random.randint(0, 1000)
        assert always(num)() == num
