"""Split Strings"""


def solution(s):
    return [x if len(x) == 2 else x + "_" for x in two_letter_segments(s)]


def two_letter_segments(s):
    for i in range(0, len(s), 2):
        yield s[i : i + 2]
