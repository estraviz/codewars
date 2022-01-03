# Multiples and Digit Sums
def procedure(i):
    return sum(sum(int(d) for d in list(str(m))) for m in range(1, 101) if m % i == 0)
