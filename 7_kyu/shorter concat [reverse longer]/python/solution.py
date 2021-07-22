"""shorter concat [reverse longer]"""


def shorter_reverse_longer(a, b):
    shorter = a if len(a) < len(b) else b
    longer = {a: b, b: a}.get(shorter)
    return shorter + longer[::-1] + shorter
