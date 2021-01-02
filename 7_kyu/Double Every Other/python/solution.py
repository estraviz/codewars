"""Double Every Other"""


def double_every_other(lst):
    return [2 * x if i % 2 else x for i, x in enumerate(lst)]
