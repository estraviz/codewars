"""Well of Ideas - Easy Version
"""


def well(x):
    num_good_ideas = x.count('good')
    return 'Publish!' if num_good_ideas in (1, 2) \
        else 'I smell a series!' if num_good_ideas > 2 else 'Fail!'
