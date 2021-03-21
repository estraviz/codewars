from random import random, randrange
from math import log, floor

from solution import isPP


def test_should_work_for_some_examples():
    assert isPP(4) == [2, 2]
    assert isPP(9) == [3, 2]
    assert isPP(5) is None


def test_should_work_for_the_first_perfect_powers():
    pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
    for item in pp:
        assert isPP(item) is not None


def test_should_work_for_random_perfect_powers():
    for i in range(100):
        m = 2 + floor(random() * 255)
        k = 2 + floor(random() * log(268435455) / log(m))
        n = m**k
        r = isPP(n)
        if r is None:
            assert r is not None
            break
        elif r[0]**r[1] != n:
            assert r[0]**r[1] == n
            break


def test_should_return_valid_pairs_for_random_inputs():
    for i in range(100):
        n = randrange(65535)
        r = isPP(n)
        if r is not None and r[0]**r[1] != n:
            assert r[0]**r[1] == n
            break
