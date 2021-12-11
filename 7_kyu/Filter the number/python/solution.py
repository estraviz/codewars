# Filter the number
import re


def filter_string(string):
    return int("".join(re.findall(r'\d+', string)))
