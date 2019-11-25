"""
Strong password
"""

from collections import defaultdict


def check_password(s):
    totals = defaultdict(int)
    if not (8 <= len(s) <= 20):
        return 'not valid'
    for c in s:
        if c.isupper():
            totals['uppercase'] += 1
        elif c.islower():
            totals['lowercase'] += 1
        elif c.isdigit():
            totals['digit'] += 1
        elif c in "!@#$%^&*?":
            totals['special'] += 1
        else:
            return 'not valid'
    if totals['uppercase'] >= 1 and totals['lowercase'] >= 1 and totals[
            'digit'] >= 1 and totals['special'] >= 1:
        return 'valid'
    return 'not valid'
