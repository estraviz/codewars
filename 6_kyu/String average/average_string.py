"""Average string
"""


def average_string(s):
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    try:
        accum = 0
        for num in s.split():
            accum += numbers[num]
        inv_numbers = {v: k for k, v in numbers.items()}
        return inv_numbers[accum//len(s.split())]
    except (KeyError, ZeroDivisionError):
        return 'n/a'
