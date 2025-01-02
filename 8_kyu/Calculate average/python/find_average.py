'''Calculate average
'''

from functools import reduce


def find_average(array):
    return reduce(lambda x, y: x + y, array)/len(array) if array else 0
