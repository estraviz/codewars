# Birthday I - Cake
from string import ascii_lowercase


def cake(candles, debris):
    if not candles:
        return "That was close!"
    score = sum(ord(c) if i % 2 == 0 else ascii_lowercase.index(c) + 1 for i, c in enumerate(debris))
    return "Fire!" if score > 0.7 * candles else "That was close!"
