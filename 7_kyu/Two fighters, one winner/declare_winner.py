"""Two fighters, one winner
"""


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
    dic = {fighter1: fighter2, fighter2: fighter1}
    if first_attacker == fighter1.name:
        attacker = fighter1
    else:
        attacker = fighter2
    victim = dic[attacker]
    while is_victim_alive(victim):
        fighter_attacks_victim(attacker, victim)
        if not is_victim_alive(victim):
            return attacker.name
        attacker = dic[attacker]
        victim = dic[victim]


def fighter_attacks_victim(attacker, victim):
    victim.health -= attacker.damage_per_attack


def is_victim_alive(victim):
    return victim.health > 0
