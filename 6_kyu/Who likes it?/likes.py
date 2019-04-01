"""Who likes it?
"""


def likes(names):
    cases = {0: 'no one likes this',
             1: '{} likes this',
             2: '{} and {} like this',
             3: '{}, {} and {} like this',
             4: '{}, {} and {others} others like this'}
    return cases[min(4, len(names))].format(*names, others=len(names)-2)
