"""Is it a Set?"""


def is_valid_set(quantities, shapes, colours, patterns):
    lengths = [
        len(set(quantities)),
        len(set(shapes)),
        len(set(colours)),
        len(set(patterns)),
    ]
    for length in lengths:
        if length not in {1, 3}:
            return False
    return True
