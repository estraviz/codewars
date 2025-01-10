def proofread(st):
    lst = str.lower(st).replace('ie', 'ei').split('. ')

    if '' in lst:
        lst.remove('')

    return '. '.join(w[0].upper() + w[1:] for w in lst)
