"""
Simple Fun #261: Whose Move
"""


def whose_move(lastPlayer, win):
    return lastPlayer if win else {
        'black': 'white',
        'white': 'black'
    }.get(lastPlayer)
