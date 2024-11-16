'''Fake Binary
'''


def fake_bin(x):
    return ''.join(['0' if int(num) < 5 else '1' for num in x])
