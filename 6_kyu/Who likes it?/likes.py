"""Who likes it?
"""


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "".join([names[0], " likes this"])
    elif len(names) == 2:
        return "".join([names[0], " and ", names[1], " like this"])
    elif len(names) == 3:
        return "".join([names[0], ", ", names[1], " and ", names[2],
                       " like this"])

    return "".join([names[0], ", ", names[1], " and ", str(len(names) - 2),
                   " others like this"])
