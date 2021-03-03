"""Logical calculator"""


def logical_calc(array, op):
    result = None
    for i, x in enumerate(array):
        if i == 0:
            result = x
        else:
            if op == "AND":
                result = result and x
            elif op == "OR":
                result = result or x
            elif op == "XOR":
                result = result ^ x
    return result
