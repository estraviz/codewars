"""Love vs friendship"""


from string import ascii_letters


def words_to_marks(s):
    return sum(ascii_letters.index(c.lower()) + 1 for c in s)
