"""String to integer conversion"""


def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return "NaN"
