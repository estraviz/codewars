"""Build a pile of Cubes
"""


def find_nb(m):
    sum = 0
    for i in range(1,m):
        sum += i**3
        if sum == m:
            return i
        if sum > m:
            return -1
