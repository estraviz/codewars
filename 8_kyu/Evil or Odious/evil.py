"""Evil or Odious
"""


def evil(n):
    return "It's Odious!" if (bin(n)[2:].count('1') % 2) else "It's Evil!"
