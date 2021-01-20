"""Array Array Array"""

import numbers


def explode(arr):
    a, b = arr[0], arr[1]
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        score = a + b
    else:
        if isinstance(a, numbers.Number):
            score = a
        elif isinstance(b, numbers.Number):
            score = b
        else:
            return "Void!"
    return [arr] * score
