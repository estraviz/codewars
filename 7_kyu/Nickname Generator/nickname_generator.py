"""
Nickname Generator
"""


def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[0:(
        4 if name[2] in "aeiou" else 3)]
