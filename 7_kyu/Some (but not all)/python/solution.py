# Some (but not all)
def some_but_not_all(seq, pred):
    return 0 < sum(map(pred, seq)) < len(seq)
