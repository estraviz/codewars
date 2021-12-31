# Check same case
def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if a.islower() and b.islower() or a.isupper() and b.isupper():
            return 1
        else:
            return 0
    return -1
