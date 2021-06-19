"""Evil Autocorrect Prank"""

import re


def autocorrect(input):
    return "".join(word for word in generator(input))


def generator(input):
    for word in re.findall( r'\w+|[^\w]+', input):
        if is_you(word) or is_longer_you(word) or is_simply_u(word):
            yield 'your sister'
        else:
            yield word


def is_you(word):
    return word.lower() == 'you'


def is_longer_you(word):
    return word.lower().startswith('youu')


def is_simply_u(word):
    return word.lower() == 'u'
