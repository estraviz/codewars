"""
Sum of a Beach
"""


def sum_of_a_beach(beach):
    return sum(beach.lower().count(word)
               for word in ["sand", "water", "fish", "sun"])
