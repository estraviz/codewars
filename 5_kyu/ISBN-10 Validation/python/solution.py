"""ISBN-10 Validation"""


def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    digits, last = isbn[:-1], isbn[-1]
    try:
        int(digits)
        if not (last == 'X' or isinstance(int(last), int)):
            raise
        return 0 == (sum((i + 1) * int(x) for i, x in enumerate(digits)) + (10 if last == 'X' else int(last)) * 10) % 11
    except Exception:
        return False
