"""
Pairs of integers from 0 to n
"""


def generate_pairs(n):
    return [[num1, num2] for num1 in range(n+1) for num2 in range(num1, n+1)]
