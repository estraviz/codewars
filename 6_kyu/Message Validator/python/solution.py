"""Message Validator"""

import re


def is_a_valid_message(message):
    if not message:
        return True

    digits = list(map(lambda x: int(x), filter(None, re.compile(r"\D").split(message))))
    alphas = list(filter(None, re.compile(r"\d").split(message)))

    try:
        int(message[0])
    except ValueError:
        alphas.pop(0)

    if len(digits) != len(alphas):
        return False

    for string, length in zip(alphas, digits):
        if len(string) != length:
            return False
    return True
