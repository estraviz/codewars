"""What century is it?
"""

suffixes = {1: 'st', 2: 'nd', 3: 'rd'}


def what_century(year):
    num = int(year[0:2]) if int(year[2:]) == 0 else int(year[0:2]) + 1
    return f'{num}{suffixes.get(num % 10, "th") if num > 20 else "th"}'
