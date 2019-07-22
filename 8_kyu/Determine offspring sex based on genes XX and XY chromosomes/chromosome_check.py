"""
Determine offspring sex based on genes XX and XY chromosomes
"""


def chromosome_check(sperm):
    dic = {'XX': "daughter", 'XY': "son"}
    return f'Congratulations! You\'re going to have a {dic.get(sperm, "cat")}.'
