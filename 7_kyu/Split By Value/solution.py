"""Split By Value
"""


def split_by_value(k, elements):
    before_k = []
    after_k = []
    for num in elements:
        if num < k:
            before_k.append(num)
        else:
            after_k.append(num)
    return before_k + after_k
