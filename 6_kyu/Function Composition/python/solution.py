"""Function Composition"""


from functools import reduce


def compose(*funcs):
    def compose_all_elems(f, g):
        return lambda *x: f(g(*x))

    return reduce(compose_all_elems, funcs)
