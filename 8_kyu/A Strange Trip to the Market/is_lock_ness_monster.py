"""
A Strange Trip to the Market
"""


def is_lock_ness_monster(string):
    for expr in ["tree fiddy", "3.50", "three fifty"]:
        if string.__contains__(expr):
            return True
    return False
