"""Is a number prime?
"""


def is_prime(num):
    if num <= 1:
        return False
    num_var = 2
    while num_var < num:
        if num % num_var == 0:
            return False
        num_var += 1
    return True
