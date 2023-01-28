import math


def circle_diameter(sides, side_length):
    return round(side_length / math.tan(math.pi / sides), 3)
