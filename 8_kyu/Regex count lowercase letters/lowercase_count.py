"""
Regex count lowercase letters
"""

import re


def lowercase_count(strng):
    return len(re.findall(r"[a-z]", strng))
