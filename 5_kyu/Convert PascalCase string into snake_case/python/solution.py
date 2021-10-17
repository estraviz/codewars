"""Convert PascalCase string into snake_case"""

from string import ascii_uppercase


def to_underscore(string):
    result = ""
    for i, c in enumerate(str(string)):
        if c in ascii_uppercase:
            result += ('_' if i != 0 and i != len(string) else '')
        result += c.lower()
    return result
