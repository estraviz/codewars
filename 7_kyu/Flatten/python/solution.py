"""Flatten"""


def flatten(lst):
    output = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                output.append(x)
        else:
            output.append(item)
    return output
