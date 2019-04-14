"""Find the odd int
"""


def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 == 1:
            return num
