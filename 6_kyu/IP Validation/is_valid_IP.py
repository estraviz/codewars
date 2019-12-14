"""
IP Validation
"""


def is_valid_IP(strng):
    octets = strng.split('.')
    if not four_elements(octets):
        return False
    for octet in octets:
        if is_invalid(octet):
            return False
    return True


def four_elements(lst):
    return len(lst) == 4


def not_all_digits(s):
    return not all(c.isdigit() for c in s)


def leading_zeros(s):
    return int(s[0]) == 0 and len(s) > 1


def octet_over_255(s):
    return int(s) > 255


def is_invalid(s):
    return not_all_digits(s) or leading_zeros(s) or octet_over_255(s)
