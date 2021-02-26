"""1RM Calculator"""


def calculate_1RM(w, r):
    if r == 1:
        return w
    elif r == 0:
        return 0
    else:
        return round(max(epley(w, r), mcglothin(w, r), lombardi(w, r)), 0)


def epley(w, r):
    return w * (1 + r / 30)


def mcglothin(w, r):
    return 100 * w / (101.3 - 2.67123 * r)


def lombardi(w, r):
    return w * r ** 0.10
