# Regexp Basics - is it a letter?
import re


def is_letter(s):
    if len(s) > 1:
        return False
    return True if re.match(r'^[A-Za-z]{1}$', s) else False
