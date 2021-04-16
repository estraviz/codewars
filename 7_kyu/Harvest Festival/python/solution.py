"""Harvest Festival"""


def plant(seed, water, fert, temp):
    stem = '-' * water
    return (stem + seed * fert) * water if 20 <= temp <= 30 else stem * water + seed
