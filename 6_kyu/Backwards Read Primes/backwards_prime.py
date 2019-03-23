"""Backwards Read Primes
"""


def backwards_prime(start, stop):
    primes = (i for i in range(start, stop + 1) if is_prime(i))
    back_primes = []
    for prime in primes:
        if is_prime(int(str(prime)[::-1])) and not is_palindrome(prime):
            back_primes.append(prime)
    return sorted(back_primes)


def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def is_palindrome(number):
    return number == int(str(number)[::-1])
