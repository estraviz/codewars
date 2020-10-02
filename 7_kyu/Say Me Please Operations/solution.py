"""Say Me Please Operations
"""

def say_me_operations(string_numbers):
    operations = []
    numbers = [int(num) for num in string_numbers.split()]
    num_1, num_2 = numbers[0:2]
    for current in numbers[2:]:
        if is_addition(num_1, num_2, current):
            operations.append('addition')
        elif is_subtraction(num_1, num_2, current):
            operations.append('subtraction')
        elif is_multiplication(num_1, num_2, current):
            operations.append('multiplication')
        elif is_division(num_1, num_2, current):
            operations.append('division')
        num_1, num_2 = num_2, current
    return ", ".join(operations)


def is_addition(n1, n2, x):
    return n1 + n2 == x


def is_subtraction(n1, n2, x):
    return n1 - n2 == x


def is_multiplication(n1, n2, x):
    return n1 * n2 == x


def is_division(n1, n2, x):
    try:
        return n1 // n2 == x
    except ZeroDivisionError:
        return False

