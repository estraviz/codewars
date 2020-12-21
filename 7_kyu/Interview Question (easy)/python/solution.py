"""Interview Question (easy)"""


from collections import Counter


def get_strings(city):
    return ",".join(
        key + ":" + "*" * value
        for key, value in dict(
            Counter(x.lower() for x in city.replace(" ", ""))
        ).items()
    )
