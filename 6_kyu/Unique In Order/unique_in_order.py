"""Unique In Order
"""


def unique_in_order(iterable):
    output = []
    if len(iterable) == 0:
        return output
    output = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != output[-1]:
            output.append(iterable[i])
    return output
