# Move 10
def move_ten(st):
    new_st = ""
    for x in st:
        if (code := ord(x) + 10) > ord('z'):
            code = code % ord('z') + ord('a') - 1
        new_st += chr(code)
    return new_st
