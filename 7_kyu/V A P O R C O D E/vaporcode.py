"""
V A P O R C O D E
"""

from string import ascii_letters


def vaporcode(s):
    str = ""
    for chr in s:
        if chr in ascii_letters:
            str += chr.upper()
        else:
            if chr == ' ':
                continue
            else:
                str += chr
    return '  '.join(str)
