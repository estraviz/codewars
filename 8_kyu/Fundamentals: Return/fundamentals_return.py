'''Fundamentals: Return
'''


def add(x, y): return x + y
# or: from operator import add


def multiply(x, y): return x*y
# or: from operator import mul as multiply


def divide(x, y): return (0 if y == 0 else x/y)
# or: from operator import div as divide


def mod(x, y): return x % y
# or: from operator import mod


def exponent(x, y): return (0 if x == 0 and y == 0 else x**y)
# or: from operator import pow as exponent


def subt(x, y): return x - y
# or: from operator import sub as subt
