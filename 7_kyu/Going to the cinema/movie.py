"""
Going to the cinema
"""

from math import ceil


def movie(card, ticket, perc):
    total_A = total_B = n = 0
    while True:
        n += 1
        total_A += ticket
        total_B += (card if n == 1 else 0) + ticket * perc**n
        if total_A > ceil(total_B):
            break
    return n
