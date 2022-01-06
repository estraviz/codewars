# Get decimal part of the given number
def get_decimal(n):
    return 0 if type(n) == int else float('0.' + str(n).split('.')[1])
