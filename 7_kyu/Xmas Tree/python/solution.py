# Xmas Tree
def xmastree(n):
    return [
        "_" * (n-i) + "#" * (2*i-1) + "_" * (n-i) for i in range(1, n+1)
        ] + 2 * ["_" * (n-1) + "#" + "_" * (n-1)]
