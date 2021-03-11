"""The Crockford Invocation"""


def add(a):
    def _wrapper(b):
        return a + b
    return _wrapper


def subtract(a):
    def _wrapper(b):
        return a - b
    return _wrapper


def multiply(a):
    def _wrapper(b):
        return a * b
    return _wrapper


def apply(fun):
    return fun
