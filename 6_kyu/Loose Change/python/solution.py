"""Loose Change"""

from enum import Enum


class Coins(Enum):
    __order__ = 'Quarters Dimes Nickels Pennies'

    Quarters = 25
    Dimes = 10
    Nickels = 5
    Pennies = 1


def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    rem = int(cents)
    for coin in Coins:
        if rem <= 0:
            break
        else:
            change_dict[coin.name], rem = divmod(rem, coin.value)
    return change_dict

