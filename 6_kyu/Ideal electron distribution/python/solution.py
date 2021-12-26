# Ideal electron distribution
def atomic_number(electrons):
    distribution = []
    n = 1
    while electrons:
        current = 2*n**2 if electrons >= 2*n**2 else electrons
        distribution.append(current)
        electrons -= current
        n += 1
    return distribution
