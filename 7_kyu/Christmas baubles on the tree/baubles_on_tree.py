"""
Christmas baubles on the tree
"""


def baubles_on_tree(baubles, branches):
    return [
        baubles // branches + (1 if branch < baubles % branches else 0)
        for branch in range(branches)
    ] if branches else "Grandma, we will have to buy a Christmas tree first!"
