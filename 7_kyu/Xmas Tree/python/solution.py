# Xmas Tree
def xmastree(n):
    return [get_row(n, i) for i in range(1, n+1)] + 2*[get_row(n, 1)]


def get_row(n, k):
    return "_"*(n-k) + "#"*(2*k-1) + "_"*(n-k)
