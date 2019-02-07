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
    rounds_fighter1 = ceil(fighter2.health/fighter1.damage_per_attack)
    rounds_fighter2 = ceil(fighter1.health/fighter2.damage_per_attack)

    if first_attacker == fighter1.name:
        if rounds_fighter2 + 1 <= rounds_fighter1:
            return fighter2.name
        return fighter1.name
    else:
        if rounds_fighter1 + 1 <= rounds_fighter2:
            return fighter1.name
        return fighter2.name
