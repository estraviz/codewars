"""Sum of odd numbers
"""


def row_sum_odd_numbers(n):
    # the complicated form in the first commit
    return n > 0 and \
           sum([num for num in range(n**2 - (n - 1), n**2 + (n + 1), 2)])
