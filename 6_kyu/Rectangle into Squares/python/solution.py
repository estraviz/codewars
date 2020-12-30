"""Rectangle into Squares"""


def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    output = []
    big, small = max(lng, wdth), min(lng, wdth)
    while min(big, small) > 0:
        output.append(small)
        tmp = big - small
        if tmp > small:
            big = tmp
        else:
            big = small
            small = tmp
    return output
