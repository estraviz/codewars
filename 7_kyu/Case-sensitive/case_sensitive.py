"""
Case-sensitive!
"""


def case_sensitive(s):
    return [
        True if len(s) == 0 or s.islower() else False,
        [c for c in s if c.isupper()]
    ]
