"""Split By Value
"""


def split_by_value(k, elements):
    return sorted(elements, key=lambda x: x < k, reverse=True)
