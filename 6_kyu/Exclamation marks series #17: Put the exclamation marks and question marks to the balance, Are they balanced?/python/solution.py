"""Exclamation marks series #17: Put the exclamation marks and question marks to the balance, Are they balanced?"""


def balance(left, right):
    l_balance = get_balance(left)
    r_balance = get_balance(right)
    if l_balance > r_balance:
        return "Left"
    elif l_balance < r_balance:
        return "Right"
    else:
        return "Balance"


def get_balance(side):
    return sum(2 if c == '!' else 3 if c == '?' else 0 for c in side)
