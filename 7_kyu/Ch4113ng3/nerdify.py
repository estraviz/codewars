"""
Ch4113ng3
"""


def nerdify(txt):
    return ''.join({
        'a': '4',
        'A': '4',
        'e': '3',
        'E': '3',
        'l': '1'
    }.get(c, c) for c in txt)
