"""Enumerable Magic #20 - Cascading Subsets"""


def each_cons(lst, n):
    output = []
    i = 0
    while i < len(lst):
        if len(subset := lst[i:i+n]) < n:
            break
        output.append(subset)
        i += 1
    return output
