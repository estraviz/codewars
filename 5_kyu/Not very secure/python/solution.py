# Not very secure
from string import ascii_letters
from string import digits


def alphanumeric(password):
    return password is not "" and \
            all(
                True if c in ascii_letters or c in digits else False
                for c in password
                )
