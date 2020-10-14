"""Weird IPv6 hex string parsing
"""


def parse_IPv6(iPv6):
    output = ""
    i = 0
    while i < len(iPv6):
        chunk = iPv6[i : i + 4]
        sum_ = 0
        for n in chunk:
            sum_ += int(n, 16)
        output += str(sum_)
        i += 5
    return output
