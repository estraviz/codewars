"""Going to zero or to infinity?
"""


def going(n):
    sum, fact = 0, 1
    for i in range(1, n+1):
        fact *= i
        sum += fact
    return int((sum/fact)*1e6)/1e6
