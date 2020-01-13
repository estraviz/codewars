"""
Loose Change!
"""

from collections import Counter

CHANGE = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25,
    'dollar': 1.0
}


def change_count(change):
    return f'${sum(CHANGE.get(type, 0)*amount for type, amount in Counter(change.split()).items()):.2f}'
