"""Name on billboard
"""


def billboard(name, price=30):
    # Your code here - note that in Python we cannot prevent the use of the
    # multiplication, but try not to be lame and solve the kata in another way!
    return sum(price for letter in name)
