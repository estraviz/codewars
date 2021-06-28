"""Sorted Union"""


def unite_unique(*lists):
    output_list = []
    for list in lists:
        for element in list:
            if element not in output_list:
                output_list.append(element)
    return output_list
