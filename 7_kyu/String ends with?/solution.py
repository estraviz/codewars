"""String ends with?
"""


def ends_with(string, ending):
    return ending in string[len(string)-len(ending):]
