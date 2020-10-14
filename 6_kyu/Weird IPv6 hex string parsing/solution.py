"""Weird IPv6 hex string parsing
"""


def parse_IPv6(iPv6):
    output = ""
    i = 0
    while i < len(iPv6):
        output += str(sum(int(n, 16) for n in iPv6[i : i + 4]))
        i += 5
    return output
