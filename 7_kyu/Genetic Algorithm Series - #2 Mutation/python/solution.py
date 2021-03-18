"""Genetic Algorithm Series - #2 Mutation"""

from random import random


def mutate(chromosome, p):
    flip = {
        '1': '0',
        '0': '1'
    }
    return "".join(flip.get(x) if p > random() else x for x in chromosome)
