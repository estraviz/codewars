"""
Define a card suit
"""


def define_suit(card):
    return {
        'C': 'clubs',
        'S': 'spades',
        'D': 'diamonds',
        'H': 'hearts'
    }.get(card[-1], None)
