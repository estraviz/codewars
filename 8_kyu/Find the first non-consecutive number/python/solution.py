def first_non_consecutive(arr):
    prev = None
    for num in arr:
        if prev is None:
            prev = num
            continue
        if prev + 1 != num:
            break
        prev = num
    else:
        return None
    return num
