"""NFL Passer Ratings"""


def passer_rating(att, yds, comp, td, ints):
    A = ((comp / att) - .3) * 5
    B = ((yds / att) - 3) * .25
    C = (td / att) * 20
    D = 2.375 - ((ints / att) * 25)

    A = get_bounded(A)
    B = get_bounded(B)
    C = get_bounded(C)
    D = get_bounded(D)

    return round(((A + B + C + D) / 6) * 100, 1)


def get_bounded(x):
    return max(min(2.375, x), 0)
