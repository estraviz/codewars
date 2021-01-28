"""Sums of Parts"""


def parts_sums(ls):
    ls_sum = sum(ls)
    result = [ls_sum]
    for i, x in enumerate(ls):
        ls_sum -= ls[i]
        result.append(ls_sum)
    return result
