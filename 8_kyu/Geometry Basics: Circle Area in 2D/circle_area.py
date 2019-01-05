'''Geometry Basics: Circle Area in 2D
'''
from math import pi


def circle_area(circle):
    return round(pi * pow(circle.radius, 2), 6)
