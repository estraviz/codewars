"""Reducing by steps"""

from math import gcd


def gcdi(x, y):
    return gcd(abs(x), abs(y))


def lcmu(a, b):
    return abs(a) * abs(b) // gcd(abs(a), abs(b))


def som(a, b):
    return a + b


def maxi(a, b):
    return max(a, b)


def mini(a, b):
    return min(a, b)


def oper_array(fct, arr, init):
    output = []
    for i, x in enumerate(arr):
        if i == 0:
            output.append(fct(init, arr[0]))
        else:
            output.append(fct(output[-1], arr[i]))
    return output
