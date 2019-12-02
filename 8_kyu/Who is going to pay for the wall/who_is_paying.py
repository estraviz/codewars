"""
Who is going to pay for the wall?
"""


def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[:2]]
