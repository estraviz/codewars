"""
Find the Integral
"""


def integrate(coefficient, exponent):
    return f'{int(coefficient / (exponent + 1))}x^{exponent + 1}'
