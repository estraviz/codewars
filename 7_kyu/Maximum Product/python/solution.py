"""Maximum Product"""


def adjacent_element_product(array):
    return max(x * y for x, y in zip(array, array[1:]))
