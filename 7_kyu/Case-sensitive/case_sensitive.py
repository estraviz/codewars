"""
Case-sensitive!
"""


def case_sensitive(s):
    return [not s or s.islower(), [c for c in s if c.isupper()]]
