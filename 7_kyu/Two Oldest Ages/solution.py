"""Two Oldest Ages
"""


def two_oldest_ages(ages):
    ages.sort()
    return [ages.pop(), ages.pop()][::-1]
