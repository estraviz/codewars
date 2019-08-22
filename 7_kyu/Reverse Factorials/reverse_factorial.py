"""
Reverse Factorials
"""


def reverse_factorial(num):
    fact = prod = 1
    while prod < num:
        fact += 1
        prod *= fact
    return f'{fact}!' if prod == num else 'None'
