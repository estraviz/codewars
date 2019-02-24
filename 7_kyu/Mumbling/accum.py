"""Mumbling
"""


def accum(s):
    return '-'.join(char_.upper() + char_.lower()*i
                    for i, char_ in enumerate(s))
