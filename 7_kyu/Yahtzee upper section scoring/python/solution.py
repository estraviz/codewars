# Yahtzee upper section scoring
from collections import Counter


def yahtzee_upper(dice):
    return max(number * times for number, times in Counter(dice).most_common())
