"""Average string
"""


def average_string(s):
    if len(s.split()) == 0:
        return "n/a"
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sum = 0
    for num in s.split():
        if num not in numbers:
            return "n/a"
        sum += numbers[num]
    for k, v in numbers.items():
        if v == sum//len(s.split()):
            return k
