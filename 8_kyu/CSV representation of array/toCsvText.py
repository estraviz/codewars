"""
CSV representation of array
"""


def toCsvText(array):
    output = ""
    for arr in array:
        for item in arr:
            output += f'{item},'
        output = output[:-1]
        output += '\n'
    return output[:-1]
