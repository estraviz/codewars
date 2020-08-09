"""Predict your age!
"""

from math import sqrt


def predict_age(*ages):
    return int(sqrt(sum(map(lambda x: x**2, ages)))/2)
