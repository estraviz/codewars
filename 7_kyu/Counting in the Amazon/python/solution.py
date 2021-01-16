"""Counting in the Amazon"""


def count_arara(n):
    adaks = " ".join(n // 2 * ["adak"])
    anane = "" if n % 2 == 0 else "anane"
    if adaks:
        if anane:
            return adaks + " " + anane
        else:
            return adaks
    else:
        return anane
