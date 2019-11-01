"""
V A P O R C O D E
"""


def vaporcode(s):
    return '  '.join(c.upper() for c in s if c != ' ')