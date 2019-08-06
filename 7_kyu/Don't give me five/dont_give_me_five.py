"""
Don't give me five!
"""


def dont_give_me_five(start, end):
    return len([num for num in range(start, end+1) if '5' not in str(num)])
