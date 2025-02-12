NULL_VECTOR = (0, 0)


def collinearity(x1, y1, x2, y2):
    return (
        is_null_vector(x1, y1) or \
        is_null_vector(x2, y2) or \
        x1*y2 == x2*y1
    )


def is_null_vector(x0, y0):
    return (x0, y0) == NULL_VECTOR
