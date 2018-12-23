from circle_circumference import circle_circumference


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def test_circle_circumference():
    digits = 6

    center = Point(10, 10)
    radius = 30
    circle = Circle(center, radius)
    assert round(circle_circumference(circle), digits) == 188.495559

    center = Point(25, -70)
    radius = 30
    circle = Circle(center, radius)
    assert round(circle_circumference(circle), digits) == 188.495559

    center = Point(-15, 5)
    radius = 0
    circle = Circle(center, radius)
    assert round(circle_circumference(circle), digits) == 0

    center = Point(-15, 5)
    radius = 12.5
    circle = Circle(center, radius)
    assert round(circle_circumference(circle), digits) == 78.539816
