"""
Exclamation marks series #6:
    Remove n exclamation marks in the sentence from left to right
"""


def remove(s, n):
    count = 0
    new_s = ""
    for i, chr in enumerate(s):
        if count == n:
            if i + 1 == len(s):
                return new_s
            else:
                return new_s + s[i:]
        else:
            if chr == '!':
                count += 1
            else:
                new_s += chr
    return new_s
