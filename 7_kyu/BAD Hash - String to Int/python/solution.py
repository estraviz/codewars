"""BAD Hash - String to Int"""


def string_hash(s):
    a = sum(ord(c) for c in s)
    b = sum(ord(y) - ord(x) for x, y in zip(s, s[1:]))
    c = (a | b) & (~a << 2)
    d = c ^ (32 * (sum(1 for c in s if c == ' ') + 1))
    return d
