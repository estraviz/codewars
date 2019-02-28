"""Growth of a Population
"""


def nb_year(p0, percent, aug, p):
    num_inhab_EoY = p0
    num_years = 0
    while num_inhab_EoY < p:
        num_years += 1
        num_inhab_EoY = (1 + percent/100)*num_inhab_EoY + aug
    return num_years
