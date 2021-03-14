"""Return the closest number multiple of 10"""


def closest_multiple_10(i):
    rem = i % 10
    return i - rem if rem < 5 else i - rem + 10