"""
Incrementer
"""


def incrementer(nums):
    output = []
    if nums:
        for i, num in enumerate(nums):
            aux = i + 1 + num
            len_aux = len(str(aux))
            if len_aux > 1:
                aux = aux % ((len_aux - 1) * 10)
            output.append(aux)
    return output
