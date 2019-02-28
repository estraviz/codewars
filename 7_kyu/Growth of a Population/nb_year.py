"""Growth of a Population
"""


def nb_year(p0, percent, aug, p):
    if p0 >= p:
        return 0
    else:
        return 1 + nb_year((1 + percent/100)*p0 + aug, percent, aug, p)
