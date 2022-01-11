# Reverse the bits in an integer
def reverse_bits(n):
    return int(bin(n)[2:][::-1], 2)
