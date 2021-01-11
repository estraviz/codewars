"""Pete, the baker"""


def cakes(recipe, available):
    return min(available.get(ingr, 0) // amnt for ingr, amnt in recipe.items())
