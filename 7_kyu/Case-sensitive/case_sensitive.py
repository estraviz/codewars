"""
Case-sensitive!
"""


def case_sensitive(s):
    return [
        True if not s or s.islower() else False, [c for c in s if c.isupper()]
    ]
