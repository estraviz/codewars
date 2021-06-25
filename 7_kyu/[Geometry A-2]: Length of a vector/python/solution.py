"""[Geometry A-2]: Length of a vector"""

import math


def vector_length(vector):
    v1x, v1y = vector[0][0], vector[0][1]
    v2x, v2y = vector[1][0], vector[1][1]
    return math.sqrt((v2x - v1x)**2 + (v2y - v1y)**2)
