def flick_switch(lst):
    result = []
    flag = True

    for elem in lst:
        if elem == "flick":
            flag = not flag
        result.append(flag)

    return result
