"""Vasya-Clerk
"""


def tickets(people):
    cash_25 = cash_50 = 0
    for bill in people:
        if bill == 25:
            cash_25 += 1
            continue
        if bill == 50:
            if cash_25 >= 1:
                cash_25 -= 1
                cash_50 += 1
                continue
            else:
                return "NO"
        if bill == 100:
            if cash_50 >= 1 and cash_25 >= 1:
                cash_50 -= 1
                cash_25 -= 1
                continue
            elif cash_25 >= 3:
                cash_25 -= 3
                continue
            else:
                return "NO"
    return "YES"
