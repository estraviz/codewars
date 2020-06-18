"""
validate code with simple regex
"""

import re


def validate_code(code):
    return bool(re.match(r'^[123]\d*$', str(code)))
