def explode(s):
    return ''.join(int(digit)*digit for digit in s)
