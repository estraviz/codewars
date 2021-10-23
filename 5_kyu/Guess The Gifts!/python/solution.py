"""Guess The Gifts!"""


def guess_gifts(wishlist, presents):
    result = []
    for i in wishlist:
        for p in presents:
            if p['size'] == i['size'] and p['clatters'] == i['clatters'] and p['weight'] == i['weight']:
                result.append(i['name'])
    return set(result)
