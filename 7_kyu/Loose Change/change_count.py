"""
Loose Change!
"""

CHANGE = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25,
    'dollar': 1.0
}


def change_count(change):
    return f'${sum(CHANGE[type_] for type_ in change.split()):.2f}'
