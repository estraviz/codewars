"""Genetic Algorithm Series - #1 Generate"""


import random


def generate(length):
    return "".join(str(random.randint(0, 1)) for _ in range(length))
