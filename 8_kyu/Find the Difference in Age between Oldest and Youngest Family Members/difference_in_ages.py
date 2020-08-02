"""
Find the Difference in Age between Oldest and Youngest Family Members
"""


def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))
