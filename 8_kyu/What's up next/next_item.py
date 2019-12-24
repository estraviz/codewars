"""
What's up next?
"""


def next_item(xs, item):
    if item in xs:
        try:
            try:
                return xs[xs.index(item) + 1]
            except IndexError:
                pass
        except AttributeError:
            try:
                return next(xs)
            except StopIteration:
                pass
