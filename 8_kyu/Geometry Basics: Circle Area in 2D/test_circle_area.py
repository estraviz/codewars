from circle_area import circle_area


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def test_circle_area():
    assert round(circle_area(Circle(Point(10, 10), 30)), 6) == 2827.433388
    assert round(circle_area(Circle(Point(25, -70), 30)), 6) == 2827.433388
    assert round(circle_area(Circle(Point(-15, 5), 0)), 6) == 0
    assert round(circle_area(Circle(Point(-15, 5), 12.5)), 6) == 490.873852
