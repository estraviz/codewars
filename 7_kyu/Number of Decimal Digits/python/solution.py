# Number of Decimal Digits
def digits(n):
    return sum(k.isdigit() for k in str(n))
