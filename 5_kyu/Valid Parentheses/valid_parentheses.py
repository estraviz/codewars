"""Valid Parentheses
"""


def valid_parentheses(string):
    count = 0
    for c in string:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
