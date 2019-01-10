"""NBA full 48 minutes average
"""


def nba_extrap(ppg, mpg):
    return 0 if mpg == 0 else round((ppg * 48) / mpg, 1)
