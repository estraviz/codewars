# Pair Zeros
def pair_zeros(arr):
    prev_zero = False
    new_arr = []
    for num in arr:
        if num == 0:
            if prev_zero is True:
                prev_zero = False
            else:
                prev_zero = True
                new_arr.append(num)
        else:
            new_arr.append(num)
    return new_arr
