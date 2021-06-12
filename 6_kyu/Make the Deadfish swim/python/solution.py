"""Make the Deadfish swim"""


def parse(data):
    output = []
    current = 0
    for x in data:
        if x == 'i':
            current += 1
        elif x == 'd':
            current -= 1
        elif x == 's':
            current *= current
        elif x == 'o':
            output.append(current)
        else:
            continue
    return output
