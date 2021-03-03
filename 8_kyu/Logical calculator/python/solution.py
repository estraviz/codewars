"""Logical calculator"""

import operator
from functools import reduce


def logical_calc(array, op):
    operation = {
        "AND": operator.__and__,
        "OR": operator.__or__,
        "XOR": operator.__xor__,
    }
    return reduce(operation.get(op), array)
