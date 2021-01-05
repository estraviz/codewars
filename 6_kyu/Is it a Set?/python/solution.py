"""Is it a Set?"""


def is_valid_set(quantities, shapes, colours, patterns):
    return all(len(set(fs)) in (1, 3) for fs in (quantities, shapes, colours, patterns))
