"""Pandemia 🌡️"""


def infected(s):
    infected = 0
    total = 0
    for continent in s.split('X'):
        if any(x == '1' for x in continent):
            infected += len(continent)
        total += len(continent)
    try:
        return 100 * infected / total
    except ZeroDivisionError:
        return 0
