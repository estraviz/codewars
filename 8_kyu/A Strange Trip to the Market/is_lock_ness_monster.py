"""
A Strange Trip to the Market
"""


def is_lock_ness_monster(string):
    return any(txt in string for txt in ["tree fiddy", "3.50", "three fifty"])
