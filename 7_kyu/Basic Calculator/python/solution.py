"""Basic Calculator"""

import operator


def calculate(num1, operation, num2):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    try:
        return ops.get(operation)(num1, num2)
    except (ZeroDivisionError, TypeError):
        pass
