"""Reverse polish notation calculator
"""
import re


def calc(expr):
    if expr == "":
        return 0
    stack = []
    for elem in expr.split():
        if re.match(r"([0-9]+)", elem):
            try:
                stack.append(int(elem))
            except ValueError:
                stack.append(float(elem))
        if re.match(r"[\+\-\*\/]", elem):
            if elem == '+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            if elem == '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            if elem == '*':
                stack.append(stack.pop(-2) * stack.pop(-1))
            if elem == '/':
                try:
                    stack.append(stack.pop(-2) / stack.pop(-1))
                except ZeroDivisionError:
                    print("Division by zero")
                    return 0
    return stack[-1]
