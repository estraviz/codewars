'''Who ate the cookie?
'''


def cookie(x):
    dic = {str: "Zach", float: "Monica", int: "Monica"}
    return "Who ate the last cookie? It was %s!" % dic.get(type(x), "the dog")
