"""
Bingo (Or Not)
"""


def bingo(array):
    chrs = list(map(lambda x: chr(x + 64), array))
    for letter in 'BINGO':
        if letter not in chrs:
            return "LOSE"
    return "WIN"
