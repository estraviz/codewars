"""
Farthest Distance
"""

from math import sqrt


def furthest_distance(arr):
    max_dist = 0
    for x1 in arr:
        for x2 in arr:
            max_dist = max(max_dist, get_distance(x1, x2))
    return round(max_dist, 2)


def get_distance(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
