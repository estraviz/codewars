"""
Draw stairs
"""


def draw_stairs(n):
    output = ''
    for i in range(n):
        if i > 0:
            output += '\n'
        output += ' ' * i + 'I'
    return output
