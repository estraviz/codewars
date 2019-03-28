"""Sum Even Fibonacci Numbers
"""


def sum_even_fibonacci(limit):
    lst = []
    a, b = 1, 2
    while True:
        if a % 2 == 0:
            lst.append(a)
        a, b = b, a + b
        if a > limit:
            break
    return sum(lst)
