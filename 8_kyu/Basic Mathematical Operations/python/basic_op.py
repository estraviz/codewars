'''
Basic Mathematical Operations
'''


def basic_op(operator, value1, value2):
    try:
        return eval("{} {} {}".format(value1, operator, value2))
    except ZeroDivisionError as ex:
        raise
