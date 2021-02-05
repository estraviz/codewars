"""Big Factorial"""


def factorial(n):
    fact = None
    if n >= 0:
        fact = 1
        if n > 0:
            while n > 1:
                fact *= n
                n -= 1
    return fact
