"""[ Code Golf ] Add 2 values for each"""


def make_new_list(l):
    return list(map(sum, zip(l, l[1:])))
