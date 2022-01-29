# Finding Remainder Without Using '%' Operator
def remainder(dividend, divisor):
    return dividend - (dividend // divisor) * divisor
