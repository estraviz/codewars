"""Kebabize"""


def kebabize(string):
    output = ""
    for c in string:
        if c.isalpha():
            if c.isupper():
                output += ('-' if len(output) else '') + c.lower()
            else:
                output += c
    return output
