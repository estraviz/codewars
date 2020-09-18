"""Write out expression!
"""

NUMBERS = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten'
}
OPERATORS = {
    '+': 'Plus ',
    '-': 'Minus ',
    '*': 'Times ',
    '/': 'Divided By ',
    '**': 'To The Power Of ',
    '=': 'Equals ',
    '!=': 'Does Not Equal '
}


def expression_out(exp):
    num1, op, num2 = exp.split(' ')
    if op not in OPERATORS:
        return "That's not an operator!"
    return f'{NUMBERS.get(num1)} {OPERATORS.get(op)}{NUMBERS.get(num2)}'
