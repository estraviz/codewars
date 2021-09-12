"""Christmas tree"""


def christmas_tree(height):
    return "\n".join(get_row(height, h) for h in range(1, height + 1))


def get_row(height, h):
    return " " * (height - h) + '*' * (2*h - 1) + " " * (height - h)
