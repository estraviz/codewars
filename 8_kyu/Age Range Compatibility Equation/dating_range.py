"""Age Range Compatibility Equation
"""
from math import floor


def dating_range(age):
    if age <= 14:
        min_age = 0.9*age
        max_age = 1.1*age
    else:
        min_age = age/2 + 7
        max_age = (age - 7)*2

    return f'{int(floor(min_age))}-{int(floor(max_age))}'
