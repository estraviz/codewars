"""
Christmas baubles on the tree
"""


def baubles_on_tree(baubles, branches):
    if branches == 0:
        return "Grandma, we will have to buy a Christmas tree first!"
    output = [baubles // branches] * branches
    for i in range(baubles % branches):
        output[i] += 1
    return output
