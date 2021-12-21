def prime_factors(n):
    factors = []
    k = 2
    while n > 1:
        if n % k == 0:
            factors.append(k)
            n /= k
        else:
            k += 1
    return factors
