"""
Reversing Words in a String
"""


def reverse(st):
    return " ".join(st.split()[::-1]).rstrip()
