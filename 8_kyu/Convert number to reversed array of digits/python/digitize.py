'''Convert number ot reversed array of digits
'''


def digitize(n):
    return [int(x) for x in str(n)][::-1]
