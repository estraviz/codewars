"""Convert PascalCase string into snake_case"""


def to_underscore(string):
    s = str(string)
    return s[0].lower() + "".join(('_' + c.lower() if c.isupper() else c) for c in s[1:])
