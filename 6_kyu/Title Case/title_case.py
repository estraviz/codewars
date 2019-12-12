"""
Title Case
"""


def title_case(title, minor_words=None):
    if minor_words is None:
        return ' '.join(word.title() for word in title.split())
    output = []
    for word in title.lower().split():
        if len(output) == 0 or word not in minor_words.lower().split():
            word = word.title()
        output.append(word)
    return ' '.join(output)
