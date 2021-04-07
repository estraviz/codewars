"""Noob Debug 1: Fix the string sum!"""


def add(s1, s2):
    return sum(s1.encode() + s2.encode())
