"""
Pole Vault Starting Marks
"""


def starting_mark(height):
    return round((height - 1.52)*(10.67 - 9.45)/(1.83 - 1.52) + 9.45, 2)
