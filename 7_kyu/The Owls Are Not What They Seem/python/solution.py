"""The Owls Are Not What They Seem"""

OWL = "''0v0''"


def owl_pic(text):
    accepted = {'8', 'W', 'T', 'Y', 'U', 'I', 'O', 'A', 'H', 'X', 'V', 'M'}
    plumage = "".join([x for x in text.upper() if x in accepted])
    return plumage + OWL + plumage[::-1]
