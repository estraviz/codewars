"""Naming Files"""


def name_file(fmt, nbr, start):
    if not isinstance(nbr, int) or nbr < 0 or not isinstance(start, int):
        return []
    elif '<index_no>' not in fmt:
        return [fmt] * nbr
    else:
        return [f"{fmt.replace('<index_no>', str(start + num))}" for num in range(nbr)]
