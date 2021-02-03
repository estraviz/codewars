"""Product of consecutive Fib numbers"""


def productFib(prod):
    F_n_1 = 0
    F_n_2 = 1
    result = False
    n = 0
    while True:
        fib = F_n_1 + F_n_2
        F_n_2 = F_n_1
        F_n_1 = fib
        temp_prod = F_n_1 * F_n_2
        if temp_prod < prod:
            continue
        else:
            if temp_prod == prod:
                result = True
            break
        n += 1
    return [F_n_2, F_n_1, result]
