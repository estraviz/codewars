"""Mr Martingale
"""


def martingale(bank, outcomes):
    stake = 100
    for win in outcomes:
        if win:
            bank += stake
            stake = 100
        else:
            bank -= stake
            stake *= 2
    return bank
