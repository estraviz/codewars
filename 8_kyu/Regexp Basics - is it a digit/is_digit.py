"""
Regexp Basics - is it a digit?
"""

import re


def is_digit(n):
    return bool(re.match(r"\d\Z", n))