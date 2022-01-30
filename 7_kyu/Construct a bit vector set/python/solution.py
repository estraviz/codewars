# Construct a bit vector set
def sort_by_bit(seq):
    return sum(2**i for i in seq)
