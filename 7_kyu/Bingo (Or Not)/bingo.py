"""
Bingo (Or Not)
"""


def bingo(array):
    return "WIN" if set("BINGO").issubset(
        set(map(lambda x: chr(x + 64), array))) else "LOSE"
