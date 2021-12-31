# Hamming Distance - Part 1: Binary codes
def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)
