"""Sum Even Fibonacci Numbers
"""


def sum_even_fibonacci(limit):
    lst = []
    for num in fib(limit):
        if num > limit:
            break
        if num % 2 == 0:
            lst.append(num)
    return sum(lst)


def fib(num):
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b
