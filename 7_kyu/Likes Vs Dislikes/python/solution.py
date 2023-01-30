def like_or_dislike(lst):
    prev = 'Nothing'
    for resp in lst:
        prev = 'Nothing' if prev == resp else resp
    return prev
