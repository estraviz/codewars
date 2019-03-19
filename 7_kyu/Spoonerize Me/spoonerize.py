"""Spoonerize Me
"""


def spoonerize(words):
    w0, w1 = words.split()
    return f'{w1[0] + w0[1:]} {w0[0] + w1[1:]}'
