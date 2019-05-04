"""Simple Pig Latin
"""


def pig_it(text):
    import string
    output = []
    for word in text.split():
        if word in string.punctuation:
            output.append(word)
        else:
            if word[-1] in string.punctuation:
                output.append("".join([word[1:-1], word[0], "ay", word[-1]]))
            else:
                output.append("".join([word[1:], word[0], "ay"]))
    return " ".join(output)
