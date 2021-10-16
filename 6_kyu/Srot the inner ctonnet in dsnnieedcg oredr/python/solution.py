"""Srot the inner ctonnet in dsnnieedcg oredr"""


def sort_the_inner_content(words):
    return " ".join(
        "".join(
            [w[0]] + (sorted(list(w[1:-1]), reverse=True) + [w[-1]] if len(w) > 1 else [])
        ) for w in words.split()
    )
