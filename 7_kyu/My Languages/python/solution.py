"""My Languages"""


from operator import itemgetter


def my_languages(results):
    tuples = sorted([(lang, score) for lang, score in results.items()
                     if score >= 60], key=itemgetter(1), reverse=True)
    return list(map(itemgetter(0), tuples))
