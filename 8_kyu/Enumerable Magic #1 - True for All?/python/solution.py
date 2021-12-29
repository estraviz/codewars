# Enumerable Magic #1 - True for All?
def _all(seq, fun):
    for x in seq:
        if x not in filter(fun, seq):
            return False
    return True
