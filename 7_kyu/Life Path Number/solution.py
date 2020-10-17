"""Life Path Number
"""

import functools


def life_path_number(birthdate):
    year, month, day = birthdate.split("-")
    number = reduce(year) + reduce(month) + reduce(day)
    while len(str(number)) > 1:
        number = reduce(number)
    return number


def reduce(n):
    return functools.reduce(lambda x, y: int(x) + int(y), list(str(n)))
