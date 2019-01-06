'''Pythagorean Triple
'''


def pythagorean_triple(integers):
    a, b, c = sorted(integers, reverse=False)
    return a**2 + b**2 == c**2
