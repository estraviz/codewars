"""
Password validator
"""

import re


def password(s):
    return True if re.search(r'[A-Z]+', s) and re.search(
        r'[a-z]+', s) and re.search(r'[\d]+', s) and len(s) >= 8 else False
