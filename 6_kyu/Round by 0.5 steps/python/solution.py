# Round by 0.5 steps

import math


def solution(n):
    decimal, integer = math.modf(n)
    if decimal < 0.25:
        return integer
    elif 0.25 <= decimal < 0.75:
        return integer + 0.5
    return integer + 1
