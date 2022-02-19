# Strange mathematics
def strange_math(n, k):
    seq = [int(x) for x in sorted(str(y) for y in range(1, n+1))]
    return seq.index(k) + 1
