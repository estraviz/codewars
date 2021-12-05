# Common Denominators
import math


def convert_fracts(lst):
    converted_fracts = []
    if lst:
        lcm = math.lcm(*[d for _, d in lst])
        converted_fracts = [[num * lcm // den, lcm] for num, den in lst]
    return converted_fracts
