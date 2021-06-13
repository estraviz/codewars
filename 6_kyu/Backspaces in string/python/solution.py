"""Backspaces in string"""

BACKSPACE = '#'


def clean_string(s):
    output = []
    for c in s:
        if c == BACKSPACE:
            if output:
                output.pop(-1)
        else:
            output.append(c)
    return "".join(output)
