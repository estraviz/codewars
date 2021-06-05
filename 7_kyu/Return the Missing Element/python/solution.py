"""Return the Missing Element"""


def get_missing_element(seq):
    seq.sort()
    for i, x in enumerate(seq):
        if i == 0:
            continue
        if x != seq[i-1] + 1:
            return x - 1
    return (x + 1) % (len(seq) + 1)
