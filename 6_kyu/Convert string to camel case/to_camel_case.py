"""Convert string to camel case
"""


def to_camel_case(text):
    text = text.replace('_', '-').split('-')
    return text[0] + "".join(x.title() for x in text[1:])
