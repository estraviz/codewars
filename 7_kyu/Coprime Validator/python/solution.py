# Coprime Validator
def are_coprime(n, m):
    return max(get_shared(get_fact(n), get_fact(m))) == 1


def get_fact(k):
    return [i for i in range(1, k+1) if k % i == 0]


def get_shared(l1, l2):
    return list(set(l1) & set(l2))
