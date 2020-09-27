"""Regex validate PIN code
"""

import re


def validate_pin(pin):
    return False if re.search(r'\D', pin) \
                 else (bool(re.match(r'^(\d{4})$', pin)) or bool(re.match(r'^(\d{6})$', pin)))
