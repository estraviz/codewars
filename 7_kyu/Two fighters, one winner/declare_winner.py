"""Two fighters, one winner
"""
from math import ceil


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(self.name, self.health,
                                            self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    fighter1.lives = ceil(fighter1.health/fighter2.damage_per_attack)
    fighter2.lives = ceil(fighter2.health/fighter1.damage_per_attack)
    if is_number_of_lives_equal(fighter1, fighter2):
        return first_attacker
    return max([fighter1, fighter2], key=lambda f: f.lives).name


def is_number_of_lives_equal(f1, f2):
    return f1.lives == f2.lives
