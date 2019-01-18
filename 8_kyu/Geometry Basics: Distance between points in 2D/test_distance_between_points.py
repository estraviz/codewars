from distance_between_points import distance_between_points
from random import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_distance_between_points_simple():
    a = Point(3, 3)
    b = Point(3, 3)
    assert distance_between_points(a, b) == 0

    a = Point(1, 6)
    b = Point(4, 2)
    assert distance_between_points(a, b) == 5

    a = Point(-10.2, 12.5)
    b = Point(0.3, 14.7)
    assert round(distance_between_points(a, b), 6) == 10.728001


def test_distance_between_points_random():
    for i in range(1000):
        a = Point(random()*100 - 50, random()*100 - 50)
        b = Point(random()*100 - 50, random()*100 - 50)
        expected = ((a.x-b.x)**2 + (a.y-b.y)**2)**0.5
        assert round(distance_between_points(a, b), 6) == round(expected, 6)
