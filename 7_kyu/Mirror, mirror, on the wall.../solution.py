"""Mirror, mirror, on the wall...
"""


def mirror(data: list) -> list:
    arr = sorted(data, reverse=False)
    return arr + arr[-2::-1]
