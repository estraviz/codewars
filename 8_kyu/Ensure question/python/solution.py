"""Ensure question"""


def ensure_question(s):
    if not s:
        return '?'
    else:
        return s if s[-1] == '?' else s + '?'
