"""Small enough? - Beginner"""


def small_enough(array, limit):
    return all(x <= limit for x in array)
