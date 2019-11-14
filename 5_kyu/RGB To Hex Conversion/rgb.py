"""
RGB To Hex Conversion
"""


def rgb(r, g, b):
    (r, g, b) = truncate([r, g, b])
    return ''.join(
        n.zfill(2)
        for n in [hex(r)[2:], hex(g)[2:], hex(b)[2:]]).upper()


def truncate(n):
    output = []
    for k in n:
        if k < 0:
            k = 0
        if k > 255:
            k = 255
        output.append(k)
    return output
