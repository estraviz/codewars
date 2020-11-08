"""Evens and Odds
"""


def evens_and_odds(n):
    return hex(n)[2:] if n % 2 else bin(n)[2:]
