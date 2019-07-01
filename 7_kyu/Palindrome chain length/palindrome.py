"""
Palindrome chain length
"""


def palindrome_chain_length(n):
    if str(n) == str(n)[::-1]:
        return 0
    return 1 + palindrome_chain_length(n + int(str(n)[::-1]))
