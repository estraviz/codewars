"""Maximum Product"""


def adjacent_element_product(array):
    max_prod = None
    for x, y in zip(array, array[1:]):
        max_prod = x * y if not max_prod else max(max_prod, x * y)
    return max_prod
