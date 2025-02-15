"""
A wolf in sheep's clothing
"""


def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return "Pls go away and stop eating my sheep"
    return f"Oi! Sheep number {queue[::-1].index('wolf')}! You are about to be eaten by a wolf!"
