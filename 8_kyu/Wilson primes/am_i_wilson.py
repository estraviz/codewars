'''
Wilson primes
'''


from math import factorial


def am_i_wilson(n):

    def am_i_prime(p):
        if p == 2:
            return True
        if p < 2 or p % 2 == 0:
            return False
        q = 3
        while(q*q <= p):
            if p % q == 0:
                return False
            q += 2
        return True

    def wilson_quotient(n):
        '''A search for Wilson primes:

        https://doi.org/10.1090/S0025-5718-2014-02800-7

        '''
        return (factorial(n-1) + 1) // n

    return am_i_prime(n) and wilson_quotient(n) % n == 0
