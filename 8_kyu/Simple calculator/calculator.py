"""
Simple calculator
"""


def calculator(x, y, op):
    if op in ['+', '-', '*', '/'] and type(x) == type(y) == int:
        return eval(f'{x} {op} {y}')
    return "unknown value"
