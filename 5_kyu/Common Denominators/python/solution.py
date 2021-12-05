# Common Denominators
from functools import reduce
from math import gcd


def convert_fracts(lst):
    converted_fracts = []
    if lst:
        lcm = reduce(lambda a, b: a * b // gcd(a, b), [d for _, d in lst])
        converted_fracts = [[num * lcm // den, lcm] for num, den in lst]
    return converted_fracts
