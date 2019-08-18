"""
Sum of squares less than some number
"""


def get_number_of_squares(n):
    sum_, count = 0, 0
    for num in range(1, n):
        sum_ += num**2
        if sum_ >= n:
            break
        else:
            count += 1
    return count
