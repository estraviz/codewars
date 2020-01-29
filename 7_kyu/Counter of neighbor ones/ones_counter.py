"""
Counter of neighbor ones
"""


def ones_counter(input):
    output = []
    count = 0
    prev = 0
    for num in input:
        if num == 0:
            if prev == 1:
                output.append(count)
                count = 0
                prev = 0
        else:
            count += 1
        prev = num
    if count:
        output.append(count)
    return output
