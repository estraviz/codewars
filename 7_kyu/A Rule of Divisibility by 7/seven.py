"""
A Rule of Divisibility by 7
"""


def seven(m):
    steps = 0
    while True:
        if m < 100:
            return (m, steps)
        m = m // 10 - 2 * (m % 10)
        steps += 1
