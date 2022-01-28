# Move 10
def move_ten(st):
    return "".join(
        chr(
            ord('a') + (ord(c) - ord('a') + 10) % (ord('z') - ord('a') + 1)
        ) for c in st
    )
