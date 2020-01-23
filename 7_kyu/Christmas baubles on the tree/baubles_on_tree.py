"""
Christmas baubles on the tree
"""


def baubles_on_tree(baubles, branches):
    if branches == 0:
        return "Grandma, we will have to buy a Christmas tree first!"
    output = [baubles // branches] * branches
    remainder = baubles % branches
    branch_index = 0
    while remainder > 0:
        output[branch_index] += 1
        remainder -= 1
        branch_index += 1
    return output
