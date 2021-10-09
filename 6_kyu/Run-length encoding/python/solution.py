"""Run-length encoding"""

from itertools import groupby


def run_length_encoding(s):
    return [[len(g), g[0]] for g in [list(g) for k, g in groupby(s)]]
