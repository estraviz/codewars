"""Training JS #18: Methods of String object--concat() split() and
   its good friend join()"""


def split_and_merge(string_, separator):
    return " ".join(separator.join(list(word)) for word in string_.split(" "))
