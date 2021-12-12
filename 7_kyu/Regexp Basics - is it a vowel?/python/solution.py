# Regexp Basics - is it a vowel?
import re


def is_vowel(s):
    if s and s[-1] == '\n':
        return False
    return True if re.match(r"^[aeiou]{1}$", s, re.IGNORECASE) else False
