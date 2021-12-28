# Find the Remainder
def remainder(a, b):
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        return None
