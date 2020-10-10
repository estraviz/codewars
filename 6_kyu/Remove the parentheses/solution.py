"""Remove the parentheses
"""

import re


def remove_parentheses(s):
    while '(' in s:
        s = re.sub(r'\([^()]*\)', '', s)
    return s
