"""Sum of the first nth term of Series
"""


def series_sum(n):
    return '0.00' if n == 0 \
                  else f'{round(sum([1/(1+3*i) for i in range(n)]), 2):.2f}'
