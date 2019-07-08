"""
Regexp Basics - is it a digit?
"""

import re


def is_digit(n):
    return True if re.match(r"^\d{1}$", re.sub(r"\n$", " ", n, 1)) else False
