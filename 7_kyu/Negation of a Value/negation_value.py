"""
Negation of a Value
"""


def negation_value(s, val):
    return not val if len(s) % 2 == 1 else not (not val)
