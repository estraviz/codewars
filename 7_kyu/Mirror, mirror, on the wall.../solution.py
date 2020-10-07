"""Mirror, mirror, on the wall...
"""


def mirror(data: list) -> list:
    arr = sorted(data, reverse=False)
    return arr if len(arr) <= 1 else arr[:-1] + arr[-1:-1] + arr[::-1]
