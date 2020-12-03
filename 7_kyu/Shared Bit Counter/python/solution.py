"""Shared Bit Counter"""


def shared_bits(a, b):
    return (
        sum(int(a_i) * int(b_i) for a_i, b_i in zip(bin(a)[2:][::-1], bin(b)[2:][::-1]))
        >= 2
    )
