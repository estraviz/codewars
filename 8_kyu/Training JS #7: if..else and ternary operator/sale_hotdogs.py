"""
Training JS #7: if..else and ternary operator
"""


def sale_hotdogs(n):
    return n*(100 if n < 5 else 90 if n >= 10 else 95)
