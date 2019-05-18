"""Valid Parentheses
"""


def valid_parentheses(string):
    if string.count('(') != string.count(')'):
        return False
    lst = []
    for c in string:
        if c == '(':
            lst.append(c)
        if c == ')':
            if not lst:
                return False
            else:
                lst.pop(0)
    return (not lst)
