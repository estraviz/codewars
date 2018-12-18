'''Calculate average
'''


def find_average(array):
    return sum(number for number in array)/len(array) if len(array) else 0
