# Divide and Conquer
def div_con(x):
    return sum(-1 * int(c) if type(c) == str else c for c in x)
