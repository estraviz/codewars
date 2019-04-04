"""Find The Parity Outlier
"""


def find_outlier(lst_int):
    mods = [num % 2 for num in lst_int]
    return lst_int[mods.index(1)] if sum(mods) == 1 else lst_int[mods.index(0)]
