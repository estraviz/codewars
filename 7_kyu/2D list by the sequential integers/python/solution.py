"""2D list by the sequential integers"""


def make_2d_list(head, row, col):
    output = []
    for _ in range(row):
        temp = []
        end = head + col
        while head < end:
            temp.append(head)
            head += 1
        output.append(temp)
    return output
