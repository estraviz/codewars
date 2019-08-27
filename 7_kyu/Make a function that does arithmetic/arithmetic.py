"""
Make a function that does arithmetic!
"""


def arithmetic(a, b, operator):
    return {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }.get(operator, 0)
