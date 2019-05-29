"""Remove the minimum
"""


def remove_smallest(numbers):
    if not numbers:
        return []
    temp = numbers.copy()
    del temp[temp.index(min(temp))]
    return temp
