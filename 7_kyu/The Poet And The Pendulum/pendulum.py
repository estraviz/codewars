from collections import deque


def pendulum(values):
    output = deque(maxlen=len(values))
    for i, value in enumerate(sorted(values)):
        if i % 2 == 0:
            output.appendleft(value)
        else:
            output.append(value)
    return list(output)
