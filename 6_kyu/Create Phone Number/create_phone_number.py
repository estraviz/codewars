"""Create Phone Number
"""


def create_phone_number(n):
    num = "".join(str(num) for num in n)
    return "({}) {}-{}".format(num[:3], num[3:6], num[6:])
