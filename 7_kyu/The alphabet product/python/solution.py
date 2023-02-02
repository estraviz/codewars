def alphabet(ns):
    lst = sorted(ns, reverse=False)
    a, b, c, ab = lst.pop(0), lst.pop(0), None, None

    for elem in lst:
        if elem == a * b and ab is None:
            ab = elem
        elif c is None:
            c = elem
        elif elem == a * c or elem == b * c:
            continue
        else:
            return elem
