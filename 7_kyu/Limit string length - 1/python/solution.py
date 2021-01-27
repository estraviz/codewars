"""Limit string length - 1"""


def solution(st, limit):
    return st[:limit] + ("..." if limit < len(st) else "")
