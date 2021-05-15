"""Dashatize it"""


DASH = '-'
EMPTY = ''


def dashatize(n):
    if n is None:
        return 'None'

    output, before, after = (EMPTY, EMPTY, EMPTY)

    try:
        str_n = str(abs(n))
        for x, y in zip(str_n, str_n[1:]):
            if output.endswith(DASH) and before == DASH:
                before = EMPTY
            output += before + x + after
            if len(output) == 1 and int(output) % 2 != 0:
                output += DASH
            before, after = (DASH, DASH) if is_odd(int(y)) else (EMPTY, EMPTY)

        if output.endswith(DASH) and before == DASH:
            before = EMPTY
        output += before + str_n[-1]
    except TypeError:
        pass
    return output


def is_odd(n):
    return n % 2
