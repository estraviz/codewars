"""zipWith"""


def zip_with(fn, a1, a2):
    return [fn(x, y) for x, y in zip(a1, a2)]
