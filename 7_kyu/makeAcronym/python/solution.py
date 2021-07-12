"""makeAcronym"""


from string import ascii_letters


def make_acronym(phrase):
    if not isinstance(phrase, str):
        return "Not a string"
    if any(x for x in phrase.replace(" ", "") if x not in ascii_letters):
        return "Not letters"
    return "".join(x[0].upper() for x in phrase.split())
