'''Is it a number?
'''

import re


def is_digit(string):
    regex = re.match(r'^[-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+)$', string.strip())
    return False if regex is None else True
