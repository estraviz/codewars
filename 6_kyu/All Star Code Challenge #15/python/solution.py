"""All Star Code Challenge #15"""


def rotate(str_):
    return [(str_ := str_[1:] + str_[0]) for _ in range(len(str_))]
