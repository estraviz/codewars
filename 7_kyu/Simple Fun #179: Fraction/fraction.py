"""
Simple Fun #179: Fraction
"""

from fractions import Fraction


def fraction(a, b):
    return Fraction(a, b).numerator + Fraction(a, b).denominator
