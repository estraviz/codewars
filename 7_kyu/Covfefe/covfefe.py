"""
Covfefe
"""


def covfefe(s):
    return s.replace('coverage',
                     'covfefe') if s.count('coverage') else s + ' covfefe'
