"""Borrower Speak"""

import re


def borrow(s):
    return re.sub(r'\W+', '', s).lower()
