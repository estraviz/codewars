'''Do I get a bonus?
'''


def bonus_time(salary, bonus):
    return "${}".format(10*salary if bonus else salary)
