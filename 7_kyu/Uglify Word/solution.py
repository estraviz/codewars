"""Uglify Word
"""


def uglify_word(s, flag=1):
    s_out = ""
    for c in s:
        if c.isalpha():
            s_out += c.upper() if flag else c.lower()
            flag = not flag
        else:
            s_out += c
            flag = 1
    return s_out
