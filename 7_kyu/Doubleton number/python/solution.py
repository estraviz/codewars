"""Doubleton number"""


def doubleton(num):
    while True:
        num += 1
        num_set = set(int(x) for x in str(num))
        if len(num_set) == 2:
            return num
