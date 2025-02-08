"""I love you, a little , a lot, passionately ... not at all
"""


def how_much_i_love_you(nb_petals):
    phrases = {0: "I love you",
               1: "a little",
               2: "a lot",
               3: "passionately",
               4: "madly",
               5: "not at all"}
    return phrases[(nb_petals - 1) % 6]
