def roots(a, b, c):
    return round(-b/a, 2) if b**2 - 4*a*c >= 0 else None
