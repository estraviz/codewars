from other_angle import other_angle
from random import randint


def test_other_angle():
    for _ in range(100):
        a_ = randint(1, 175)
        b_ = randint(1, 180 - a_)
        c_ = 180 - a_ - b_
        assert other_angle(a_, b_) == c_
