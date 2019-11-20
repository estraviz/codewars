"""
Mexican Wave
"""


def wave(str):
    return [
        str[:i] + str[i].upper() + str[i + 1:] for i in range(len(str))
        if str[i].isalpha()
    ]
