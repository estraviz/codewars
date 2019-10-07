"""
Longest vowel chain
"""


def solve(s):
    count = max_count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count
