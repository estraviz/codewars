from subtract_sum import subtract_sum
from random import randint


def test_subtract_sum():
    assert subtract_sum(10) == "apple"


def test_random():
    def tester(n):
        assert subtract_sum(n) == "apple"

    for _ in range(100):
        tester(randint(11, 10000))
