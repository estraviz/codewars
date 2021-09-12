"""Christmas tree"""


def christmas_tree(height):
    return "\n".join(" " * (height - h) + '*' * (2*h - 1) + " " * (height - h) for h in range(1, height + 1))
