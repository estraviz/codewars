"""
How many stairs will Suzuki climb in 20 years?
"""


def stairs_in_20(stairs):
    return 20*sum(sum(weekday) for weekday in stairs)
