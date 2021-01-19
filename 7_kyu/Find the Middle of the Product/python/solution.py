"""Find the Middle of the Product"""

import re
from operator import mul
from functools import reduce


def find_middle(string):
    if not string or type(string) != str:
        return -1

    numbers = "".join(re.findall("[0-9]+", string))
    if not numbers:
        return -1

    digits = [int(number) for number in numbers]
    product = str(reduce(mul, digits, 1))

    _len = len(product)
    if _len % 2:
        return int(product[_len // 2])
    else:
        return int(product[_len // 2 - 1 : _len // 2 + 1])
