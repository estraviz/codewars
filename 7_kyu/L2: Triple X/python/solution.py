"""L2: Triple X"""


def triple_x(s):
    try:
        return s[(ind := s.index("x")) : ind + 3] == "xxx"
    except ValueError:
        return False
