'''Multiplication table for number
'''


def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))
