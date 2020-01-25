"""
Same Birthday Probability
"""

from math import factorial


def calculate_probability(n):
    return 1 if n > 365 else round(
        1 - factorial(365) / (factorial(365 - n) * 365**n), 2)
