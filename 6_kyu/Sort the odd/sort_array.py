"""Sort the odd
"""


def sort_array(source_array):
    odd = []
    for i, elem in enumerate(source_array):
        if elem % 2 == 1:
            odd.append(elem)
            source_array[i] = 'x'
    odd.sort()
    for i, elem in enumerate(source_array):
        if elem == 'x':
            source_array[i] = odd.pop(0)
    return source_array
