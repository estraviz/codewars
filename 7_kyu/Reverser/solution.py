def reverse(n):
    i = 0
    coefs = []
    while n > 0:
        coefs.append(n % 10)
        n //= 10
        i += 1
    return sum(10 ** i * k for i, k in enumerate(coefs[::-1]))
