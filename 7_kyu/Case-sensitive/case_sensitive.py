"""
Case-sensitive!
"""


def case_sensitive(s):
    output = [c for c in s if c.isupper()]
    return [True if not output else False, output]
