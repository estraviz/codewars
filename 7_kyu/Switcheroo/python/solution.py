# Switcheroo
def switcheroo(s):
    return s.translate(s.maketrans({'a': 'b', 'b': 'a'}))
